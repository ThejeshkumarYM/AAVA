from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException
import time

service = Service('path/to/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.testrail.com/")
    time.sleep(5)  # Wait for page to load
    if "TestRail" in driver.title:
        print("Status Report: ---------Success---------")
        print("Chrome opened with URL: https://www.testrail.com/")
        print("Error Log: None")
    else:
        print("Status Report: ---------Failure---------")
        print("Error Log: Unexpected page title or content.")
except (WebDriverException, TimeoutException) as e:
    print("Status Report: ---------Failure---------")
    print(f"Error Log: {str(e)}")
finally:
    driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def chrome_browser():
    # Initialize and return a Chrome WebDriver instance
    driver = webdriver.Chrome()
    return driver

def open_platform(driver):
    driver.get('https://www.testrail.com/')
    time.sleep(5)
    element = driver.find_element(By.ID, 'hs-nav-v4--main-cta-book-a-demo')
    element.click()

if __name__ == '__main__':
    driver = chrome_browser()
    try:
        open_platform(driver)
        # Add any validations or further steps here if required
    finally:
        driver.quit()
