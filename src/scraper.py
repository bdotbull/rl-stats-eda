"""
bdotbull
Web Scraper for ballchasing.com using ballchasing API
"""

# Imports
import requests

# API Base Path
api_base_url = 'https://ballchasing.com/api/'

# Authorization token for ballchasing.com API
token_file_path = '../creds/ballchasing_credentials.txt'
with open(token_file_path, 'r') as tfp:
    token = tfp.readlines()[0]

# Data output path
data_out_path = ''


headers = {
    'Authorization': token
}

data = {
    'pro': True,
    'count' : 3
}

endpoint = f"{api_base_url}"

def ping_api():
    '''
    Checks if API key is correct and ballchasing API is reachable
    '''
    return requests.get(api_base_url, headers=headers).status_code

def get_replay_list(data):
    endpoint = f"{api_base_url}replays"
    return (requests.get(endpoint, headers=headers, data=data).json())




if __name__ == '__main__':
    print(f"Ping Response: {ping_api()}")
    print(get_replay_list(data))