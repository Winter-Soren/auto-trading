import json
import requests

url = "https://api.upstox.com/v2/option/contract"

payload = {}

params = {
    'instrument_key': 'NSE_INDEX|Nifty 50'
}

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiIwMEEwUEEiLCJqdGkiOiI2NWU4YWNlNzcyY2QwMzM0ODA5Nzk5OTUiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNBY3RpdmUiOnRydWUsInNjb3BlIjpbImludGVyYWN0aXZlIiwiaGlzdG9yaWNhbCJdLCJpYXQiOjE3MDk3NDc0MzEsImlzcyI6InVkYXBpLWdhdGV3YXktc2VydmljZSIsImV4cCI6MTcwOTc2MjQwMH0.Ce26aQLsNuRvYNg9jUwghQ4ZIm8vZzcndvMgfI-yWtw'
}

response = requests.request("GET", url, headers=headers, params=params)

# Check if request was successful (status code 200)
if response.status_code == 200:
    # Save response JSON data to a file
    with open("response.json", "w") as json_file:
        json.dump(response.json(), json_file)
    print("Response saved to response.json.")
else:
    print("Error:", response.status_code)
