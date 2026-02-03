from selenium import webdriver
from selenium.webdriver.common.by import By

def chrome_browser():
    driver = webdriver.Chrome()
    return driver

def open_platform(driver):
    driver.get('https://www.testrail.com/')
    # Wait for the page to load and locate the element by ID
    element = driver.find_element(By.ID, 'header-navbar')
    # Example interaction: print the element's text
    print(element.text)
    # You can add additional interactions here if needed

# Example usage
if __name__ == '__main__':
    driver = chrome_browser()
    open_platform(driver)
    driver.quit()
