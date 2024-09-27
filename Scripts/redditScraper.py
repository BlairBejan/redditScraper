import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import datetime
import json
import os

#import data from config file
config_path = os.path.join(os.path.dirname(__file__),
                           '../Config/config.json')
content_out = os.path.join(os.path.dirname(__file__),
                           '../Logs/out.log')
with open(config_path, 'r') as config_file:
    config = json.load(config_file)

url = config['url']
user_url = config['user_url']
headers = config['headers']
last_run = datetime.datetime.fromisoformat(config['last_run'])




def make_request(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as error:
        print(f"Error making request to {url}: {error}")
        return None
    
def scrape_data(url, headers, last_run):
    content = make_request(url, headers)
    if content:
        soup = BeautifulSoup(content, 'html.parser')
        posts = soup.find_all('div', class_='thing')
        for post in posts:
            #this is a check to see if a post is an ad
            comments_element = post.find('a', class_='bylink comments may-blank')
            if comments_element is not None:
                time_tag = post.find('time')
                post_time = time_tag['datetime']
                formatted_post_time = datetime.datetime.fromisoformat(post_time)
                print("post time")
                print(formatted_post_time)
                if formatted_post_time > last_run:
                    data = {
                        "reddit_post_id": post['data-fullname'].split('_')[-1],
                        "title": post.find('p', class_='title').a.text,
                        "author_name": post.find('p', class_='tagline').a.text,
                        "upvotes": post.find('div', class_='score unvoted').text,
                        "comments_url": urljoin(url, comments_element['href']),
                        "author_url": urljoin(user_url, post.find('p', class_='tagline').a.text)
                        }
                    with open(content_out, 'r+') as content_out_file:
                        existing_data = json.load(content_out_file)
                        existing_data.append(data)
                        content_out_file.seek(0)
                        json.dump(existing_data, content_out_file, indent=4)
                        content_out_file.truncate()
                else: return

    
scrape_data(url, headers, last_run)

now = datetime.datetime.now(datetime.timezone.utc)

config['last_run'] = now.strftime('%Y-%m-%d %H:%M:%S%z')

with open(config_path, 'w') as config_file:
    json.dump(config, config_file, indent=4)