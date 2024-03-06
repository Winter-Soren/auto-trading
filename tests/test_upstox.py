
import time
import requests


from config import UPSTOX_API_KEY, UPSTOX_API_SECRET, UPSTOX_REDIRECT_URI, UPSTOX_MOBILE_NUMBER, UPSTOX_PIN, UPSTOX_AUTH_URL

global_access_code = None
global_access_token = None






def place_order(access_token = None):
    url = 'https://api.upstox.com/v2/order/place'
    headers = {
        # 'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + 'eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiIwMEEwUEEiLCJqdGkiOiI2NWU4YWNlNzcyY2QwMzM0ODA5Nzk5OTUiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNBY3RpdmUiOnRydWUsInNjb3BlIjpbImludGVyYWN0aXZlIiwiaGlzdG9yaWNhbCJdLCJpYXQiOjE3MDk3NDc0MzEsImlzcyI6InVkYXBpLWdhdGV3YXktc2VydmljZSIsImV4cCI6MTcwOTc2MjQwMH0.Ce26aQLsNuRvYNg9jUwghQ4ZIm8vZzcndvMgfI-yWtw',
    }

    data = {
        'quantity': 1,
        'product': 'D',
        'validity': 'DAY',
        'price': 0,
        'tag': 'string',
        'instrument_token': 'NSE_FO|56843',
        'order_type': 'MARKET',
        'transaction_type': 'BUY',
        'disclosed_quantity': 0,
        'trigger_price': 0,
        'is_amo': False,
    }

    try:
        # Send the POST request
        response = requests.post(url, json=data, headers=headers)

        # Print the response status code and body
        print('Response Code:', response.status_code)
        print('Response Body:', response.json())

    except Exception as e:
        # Handle exceptions
        print('Error:', str(e))





if __name__ == "__main__":
    # global_access_code = get_access_code()
    # global_access_token = get_access_token()
    # place_order(global_access_token)
    place_order()

