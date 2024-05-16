import re
import jieba
import spacy
import pandas as pd
from neo4j import GraphDatabase

# 假设数据存储在articles.csv文件中
data = pd.read_csv('../zhihu/data/articles.csv', encoding='utf-8')

# 使用中文停用词表
stop_words = set()
with open('stopwords.txt', 'r', encoding='utf-8') as f:
    stop_words = set(f.read().splitlines())


def preprocess_text(text):
    # 移除HTML标签
    text = re.sub(r'<.*?>', '', text)
    # 移除非中文字符（保留汉字、字母和数字）
    text = re.sub(r'[^\u4e00-\u9fffA-Za-z0-9]', '', text)
    # 分词
    words = jieba.lcut(text)
    # 移除停用词
    text = ' '.join([word for word in words if word not in stop_words])
    return text


# 合并title和content列，并进行预处理
data['merged_text'] = (data['title'].fillna('') + ' ' + data['content'].fillna('')).apply(preprocess_text)

# 加载spacy中文模型
nlp = spacy.load('zh_core_web_sm')


def extract_entities_relations(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    relations = []
    # 提取关系的简单例子，可以根据具体需求扩展
    for token in doc:
        if token.dep_ in ('nsubj', 'dobj'):
            relations.append((token.head.text, token.dep_, token.text))
    return entities, relations


# 提取实体和关系
data['entities_relations'] = data['merged_text'].apply(lambda x: extract_entities_relations(x))

# 分离实体和关系
data['entities'] = data['entities_relations'].apply(lambda x: x[0])
data['relations'] = data['entities_relations'].apply(lambda x: x[1])

print(data[['entities', 'relations']])

# Neo4j数据库连接设置
uri = "bolt://101.37.253.225:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "demouser"))


def create_entity(tx, entity_text, entity_label):
    tx.run("MERGE (e:Entity {text: $text, label: $label})", text=entity_text, label=entity_label)


def create_relation(tx, head, relation, tail):
    tx.run("""
        MATCH (h:Entity {text: $head})
        MATCH (t:Entity {text: $tail})
        MERGE (h)-[r:RELATION {type: $relation}]->(t)
    """, head=head, tail=tail, relation=relation)


def add_data_to_neo4j(data):
    with driver.session() as session:
        for _, row in data.iterrows():
            for entity, label in row['entities']:
                session.write_transaction(create_entity, entity, label)
            for head, relation, tail in row['relations']:
                session.write_transaction(create_relation, head, relation, tail)

# add_data_to_neo4j(data)