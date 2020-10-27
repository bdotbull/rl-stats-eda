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
def replay_to_mongo_collection(collection, replay_json):
    collection.insert_one(replay_json)

def get_all_replays(collection, replay_id_list):
    for rep in replay_id_list:
        try:
            replay_to_mongo_collection(collection, get_specific_replay(rep))
        except DuplicateKeyError:
            print (f'Error: Duplicate entry in {collection} with {rep}')


# Variable Declaration
api_base_url = 'https://ballchasing.com/api/'

# Authorization token for ballchasing.com API
token_file_path = '../creds/ballchasing_credentials.txt'
with open(token_file_path, 'r') as tfp:
    token = tfp.readlines()[0]
headers = { 'Authorization': token }

# Define MongoDB database and collection
db_client = MongoClient('localhost', 27017)
db = db_client['rocket_league']
collection = db['rl_replays']

# when clean, new collection in rocket_league database


if __name__ == '__main__':
    # kwargs for replay list test
    data = {
        'pro': True,
        'count' : 200
    }

    print(f"Ping Response: {ping_api()}")
    
    ## MAIN
    '''wrap whole thing in while loop until 10000 replays'''
    # get list of replays using data->list as filter
    get_replay_list(data)

    # check if any replays in list are in collection already
        # remove dupes from list
    
    # for replay in replay_list
        # get_specific_replay
        # add replay to mongoDB
