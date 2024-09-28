from pymongo import MongoClient
import os

client = MongoClient('mongodb://localhost:27017/')
db = client['scraping_db']

def save_posts(data):
    print("data in db function")
    print(data)
    collection = db['Posts']
    collection.insert_one(data)
