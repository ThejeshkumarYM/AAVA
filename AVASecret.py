from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException
import time

print("thejesh")

def create_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)


def test_google(driver):
    driver.get("https://www.google.com")
    print("Google title:", driver.title)


def test_testrail(driver):
    try:
        driver.get("https://www.testrail.com/")
        time.sleep(5)

        if "TestRail" in driver.title:
            print("Status Report: ---------SUCCESS---------")
            print("Chrome opened with URL: https://www.testrail.com/")
            print("Error Log: None")
        else:
            print("Status Report: ---------FAILURE---------")
            print("Error Log: Unexpected page title")

    except (WebDriverException, TimeoutException) as e:
        print("Status Report: ---------FAILURE---------")
        print(f"Error Log: {e}")


def test_book_demo_button(driver):
    driver.get("https://www.testrail.com/")
    time.sleep(5)

