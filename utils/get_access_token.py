import requests
from config.config import UPSTOX_API_KEY, UPSTOX_API_SECRET, UPSTOX_REDIRECT_URI, UPSTOX_AUTH_URL

def get_access_token(access_code: str):
    session = requests.Session()
    
    headers = {
        "accept": "application/json", 
        "Api-Version": "2.0", 
        "content-type": "application/x-www-form-urlencoded"
    }
    
    data = {
        'code': access_code,
        'client_id': UPSTOX_API_KEY,
        'client_secret': UPSTOX_API_SECRET,
        'redirect_uri': UPSTOX_REDIRECT_URI,
        'grant_type': 'authorization_code'
    }

    response = session.post(url=UPSTOX_AUTH_URL, headers=headers, data=data)
    assert response.status_code == 200, f"Error in r3:\n {response.json()}"
    
    json_response = response.json()
    access_token = json_response['access_token']
    print("Access token: ",access_token)
    return access_token