import os
from datetime import datetime
import json

def read_config():
    config_path = os.path.join(os.path.dirname(__file__), '../Config/config.json')
    
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)

    url = config['url']
    user_url = config['user_url']
    headers = config['headers']
    last_runtest = config['last_run']
    last_run = datetime.strptime(last_runtest, '%Y-%m-%d %H:%M:%S%z')
    return(url, user_url, headers, last_run)