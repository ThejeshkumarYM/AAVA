from selenium import webdriver
from selenium.webdriver.common.by import By

def chrome_browser():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    return driver

def open_platform(driver):
    # Open the TestRail platform
    driver.get('https://www.testrail.com/')
    
    # Locate the web element by ID and interact with it
    element = driver.find_element(By.ID, 'navbarNavDropdown')
    element.click()
    
    # Additional interactions can be added here if needed

# Example usage
if __name__ == '__main__':
    driver = chrome_browser()
    open_platform(driver)
    driver.quit()
