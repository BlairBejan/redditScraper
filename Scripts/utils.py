import os
from datetime import datetime
import json
import requests
from bs4 import BeautifulSoup

def read_config():
    config_path = os.path.join(os.path.dirname(__file__), '../Config/config.json')
    
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return(config)

def get_soup(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except requests.exceptions.RequestException as error:
        print(f"Error making request to {url}: {error}")
        return None

'''
get_soup("https://old.reddit.com/r/uspolitics/new/", {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    })
read_config()
'''