import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import datetime
import json
import os

#import data from config file
config_path = os.path.join(os.path.dirname(__file__),
                           '../Config/config.json')
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
    


print(f"Script executed at: {datetime.datetime.now()}")

config['last_run'] = datetime.datetime.now().isoformat()
with open(config_path, 'w') as config_file:
    json.dump(config, config_file, indent=4)
