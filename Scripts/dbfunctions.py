from pymongo import MongoClient


def save_posts(data):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['scraping_db']
    print("data in db function")
    print(data)
    collection = db['Posts']
    collection.insert_one(data)


def get_posts():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['scraping_db']
    posts_collection = db['Posts']
    print(posts_collection)
    posts = posts_collection.find({})
    return posts
