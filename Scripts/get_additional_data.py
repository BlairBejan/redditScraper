from pymongo import MongoClient
from redditScraper import make_request
import requests
import json
import os
from bs4 import BeautifulSoup


config_path = os.path.join(os.path.dirname(__file__),
                           '../Config/config.json')
with open(config_path, 'r') as config_file:
    config = json.load(config_file)

user_url = config['user_url']
headers = config['headers']

def getposts():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['scraping_db']
    posts_collection = db['Posts']
    print(posts_collection)
    posts = posts_collection.find({})
    client.close()
    return posts

def make_request(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as error:
        print(f"Error making request to {url}: {error}")
        return None
    
def parseposts(posts):
    for post in posts:
        content = make_request(user_url, headers=headers)
        if content:
            soup = BeautifulSoup(content, 'html.parser')



posts = getposts()
parseposts(posts)
