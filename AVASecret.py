from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def chrome_browser():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()
    return driver

def open_platform(driver):
    # Open the TestRail homepage
    driver.get('https://www.testrail.com/')
    # Wait for the page to load (simple sleep for demonstration; explicit waits are preferred in production)
    time.sleep(3)
    # Locate the web element by ID
    element = driver.find_element(By.ID, 'header-navbar')
    # Interact with the element (for demonstration, we'll print its text)
    print("Header Navbar Text:", element.text)
    # Example interaction: scroll element into view
    driver.execute_script("arguments[0].scrollIntoView();", element)
    # Add additional interactions as needed

# Example usage
if __name__ == '__main__':
    driver = chrome_browser()
    try:
        open_platform(driver)
    finally:
        driver.quit()
