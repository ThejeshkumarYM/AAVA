from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def chrome_browser():
    driver = webdriver.Chrome()
    return driver

def open_platform(driver):
    driver.get('https://www.testrail.com/')
    # Wait for the page to load
    time.sleep(2)
    element = driver.find_element(By.ID, 'header-navbar')
    # Example interaction: print the text of the header navbar
    print("Header Navbar Text:", element.text)
    # You can add additional interactions here, for example:
    # element.click()
    # Take a screenshot for validation
    driver.save_screenshot('testrail_homepage.png')

# Example usage
if __name__ == '__main__':
    driver = chrome_browser()
    try:
        open_platform(driver)
    finally:
        driver.quit()
