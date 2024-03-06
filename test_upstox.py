
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from config import UPSTOX_API_KEY, UPSTOX_API_SECRET, UPSTOX_REDIRECT_URI, UPSTOX_MOBILE_NUMBER, UPSTOX_PIN, UPSTOX_AUTH_URL

global_access_code = None
global_access_token = None

def get_access_code():
    print("loading the webdriver")
    # Selenium loads the chrome driver
    driver = webdriver.Chrome()
    # driver fetches the url along with api and secret key
    driver.get(
        f'https://api-v2.upstox.com/login/authorization/dialog?response_type="code"&client_id={UPSTOX_API_KEY}&redirect_uri={UPSTOX_REDIRECT_URI}')
    print(driver.title)
    # to minimize the browser window
    print("minimizing the window")
    driver.minimize_window()
    # driver.implicitly_wait(10)
    # searches for the html element for mobile number
    print("searching for the mobile number")
    phone_no = driver.find_element(By.ID, "mobileNum")
    # passes the mobile number 
    print("passing the mobile number")
    phone_no.send_keys(UPSTOX_MOBILE_NUMBER)
    # Searches for the Get OTP button on the page
    print("searching for the get otp button")
    get_otp_btn = driver.find_element(By.ID, "getOtp")
    # Submits the get OTP button on the page
    print("submitting the get otp button")
    get_otp_btn.submit()
    driver.implicitly_wait(1)
    # time.sleep(20)
    # Searches for the OTP Number element
    print("searching for the otp number")
    otp = driver.find_element(By.ID, "otpNum")
    #Calls the get otp function and passes the otp to the OTP NUM field
    # otp.send_keys(email_otp.get_otp())
    # get the otp from user
    otp.send_keys(input("Enter OTP: "))
    # Searches the continue button on the page
    continue_btn = driver.find_element(By.ID, "continueBtn")
    #Submits the continue button
    continue_btn.submit()
    # driver.implicitly_wait(10)
    # Searches for Pin element
    print("searching for the pin")
    pin = driver.find_element(By.ID, "pinCode")
    # driver.implicitly_wait(10)
    # Passes the pin from the config file
    pin.send_keys(UPSTOX_PIN)
    # Searches the Continue Button
    submit = driver.find_element(By.ID, "pinContinueBtn")
    # Submits the Pin
    submit.click()
    
    time.sleep(1)
    # Redirect url contains the access code and it is split from the url
    url = driver.current_url
    print(url)
    initial_access_code = url.split('code=')[1]
    access_code = initial_access_code.split('&')[0]
    print(access_code)
    driver.close()
    print("Access Code: ", access_code)
    return access_code

# function to fetch the access token
def get_access_token():
    s = requests.Session()
    access_code = get_access_code()
    # header data that needs to be sent to the post method
    headers = {"accept": "application/json", "Api-Version": "2.0", "content-type": "application/x-www-form-urlencoded"}
    # the main data that needs to be sent to the post method
    data = {'code': access_code,
            'client_id': UPSTOX_API_KEY,
            'client_secret': UPSTOX_API_SECRET,
            'redirect_uri': UPSTOX_REDIRECT_URI,
            'grant_type': 'authorization_code'
            }
    # post method consists of three parameters url, header and data
    resp = s.post(url=UPSTOX_AUTH_URL, headers=headers, data=data)
    # test for the status code else throws error
    assert resp.status_code == 200, f"Error in r3:\n {resp.json()}"
    
    json_response = resp.json()
    # read the access token from the json response
    access_token = json_response['access_token']
    # write the access token to the text file
    print("Access token: ",access_token)
    return access_token


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

