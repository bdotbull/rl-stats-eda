"""
bdotbull
Web Scraper for ballchasing.com using ballchasing API
"""

# Imports

# Authorization token for ballchasing.com API
def get_auth_token():
    token_file_path = '../creds/ballchasing_credentials.txt'
    with open(token_file_path, 'r') as tfp:
        token = tfp.readlines()[0]
    return token

# Data output path
data_out_path = ''
