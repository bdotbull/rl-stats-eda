"""
bdotbull
Web Scraper for ballchasing.com using ballchasing API
"""

# Imports
import requests
import time
from requests.api import get
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


# Function Definitions
def ping_api():
    '''
    Checks if API key is correct and ballchasing API is reachable
    '''
    return requests.get(api_base_url, headers=headers).status_code

def get_replay_list(data):
    endpoint = f"{api_base_url}replays"
    return requests.get(endpoint, headers=headers, data=data).json()

def get_specific_replay(replay_id):
    endpoint = f"{api_base_url}replays/{replay_id}"
    return requests.get(endpoint, headers=headers).json()

# pipe specific replay to MongoDB
def replay_to_mongo(replay_json):
    pass

def get_all_replays(replay_id_list):
    pass


# Variable Declaration
api_base_url = 'https://ballchasing.com/api/'

# Authorization token for ballchasing.com API
token_file_path = '../creds/ballchasing_credentials.txt'
with open(token_file_path, 'r') as tfp:
    token = tfp.readlines()[0]

headers = {
    'Authorization': token
}

# Define MongoDB database and table
db_client = MongoClient()
db = db_client['']
table = db['']


if __name__ == '__main__':
    # kwargs for replay list test
    data = {
        'pro': True,
        'count' : 3
    }
    
    # Print Tests
    print(f"Ping Response: {ping_api()}")
    
    #print(get_replay_list(data))
    
    test_replay_id = '56889c3e-c420-45db-92fd-47ce2a3604b0'
    print(get_specific_replay(test_replay_id))