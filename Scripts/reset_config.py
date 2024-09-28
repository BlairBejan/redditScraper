from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['scraping_db']



posts_collection = db['Posts']
users_collection = db['Users']
comments_collection = db['Comments']

posts_result = posts_collection.delete_many({})
users_result = users_collection.delete_many({})
comments_result = comments_collection.delete_many({})

print(f"Deleted {posts_result.deleted_count} posts.")
print(f"Deleted {users_result.deleted_count} users.")
print(f"Deleted {comments_result.deleted_count} comments.")