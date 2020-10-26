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
    'pro': True
}
endpoint = f"{api_base_url}"

def ping_api():
    '''
    Checks if API key is correct and ballchasing API is reachable
    '''
    return requests.get(api_base_url, headers=headers).status_code

if __name__ == '__main__':
    #r = requests.get(endpoint, headers=headers)
    #print(r.status_code)
    print(ping_api())