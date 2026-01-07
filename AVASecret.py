from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def chrome_browser():
    driver = webdriver.Chrome()
    return driver

def open_platform(driver):
    # Open the TestRail homepage
    driver.get('https://www.testrail.com/')
    
    # Optional: Wait for the page to load
    time.sleep(3)
    
    # Locate the web element by ID and interact with it (e.g., click or print text)
    element = driver.find_element(By.ID, 'header-navigation')
    
    # Example interaction: Print the element's text content
    print("Header navigation text:", element.text)
    
    # Example interaction: You can also click if it's clickable
    # element.click()
    
    # Optional: Take a screenshot for verification
    driver.save_screenshot('testrail_homepage.png')

# Example usage
if __name__ == '__main__':
    driver = chrome_browser()
    try:
        open_platform(driver)
    finally:
        driver.quit()
