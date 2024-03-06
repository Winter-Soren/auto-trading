from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from typing import Optional
from ..config import UPSTOX_API_KEY, UPSTOX_REDIRECT_URI, UPSTOX_MOBILE_NUMBER, UPSTOX_PIN

def get_access_code() -> Optional[str]:
    print("loading the webdriver")
    driver = webdriver.Chrome()
    driver.get(f'https://api-v2.upstox.com/login/authorization/dialog?response_type="code"&client_id={UPSTOX_API_KEY}&redirect_uri={UPSTOX_REDIRECT_URI}')
    print(driver.title)

    print("minimizing the window")
    driver.minimize_window()

    print("searching for the mobile number")
    phone_no = driver.find_element(By.ID, "mobileNum")

    print("passing the mobile number")
    phone_no.send_keys(UPSTOX_MOBILE_NUMBER)

    print("searching for the get otp button")
    get_otp_btn = driver.find_element(By.ID, "getOtp")

    print("submitting the get otp button")
    get_otp_btn.submit()
    driver.implicitly_wait(1)

    print("searching for the otp number")
    otp = driver.find_element(By.ID, "otpNum")

    otp.send_keys(input("Enter OTP: "))
    continue_btn = driver.find_element(By.ID, "continueBtn")
    continue_btn.submit()

    print("searching for the pin")
    pin = driver.find_element(By.ID, "pinCode")
    pin.send_keys(UPSTOX_PIN)
    submit = driver.find_element(By.ID, "pinContinueBtn")

    submit.click()
    
    time.sleep(1)
    
    url = driver.current_url
    print(url)
    initial_access_code = url.split('code=')[1]
    access_code = initial_access_code.split('&')[0]
    print(access_code)
    driver.close()

    print("Access Code: ", access_code)
    return access_code