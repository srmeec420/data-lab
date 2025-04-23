# pip install pymongo

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['vysya_db'] 
collection = db['mca_collection']  

sample_data = [
    {"name": 'John Doe', 'age': 25},  
    {"name": 'James', 'age': 44} 
]

collection.insert_many(sample_data)

records = collection.find()

for record in records:
    print(record)
