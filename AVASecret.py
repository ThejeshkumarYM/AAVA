from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def chrome_browser():
    # Initialize and return a Chrome WebDriver instance
    driver = webdriver.Chrome()
    return driver

def open_platform(driver):
    # Open the TestRail homepage
    driver.get('https://www.testrail.com/')
    # Wait for page to load (simple static wait for demonstration; use WebDriverWait for production code)
    time.sleep(3)
    # Locate the "Login" button by its ID and click it
    login_button = driver.find_element(By.ID, 'menu-login-button')
    login_button.click()
    # Additional interactions can be added here if needed

# Example usage
if __name__ == '__main__':
    driver = chrome_browser()
    try:
        open_platform(driver)
        # Optionally, add more steps or assertions here
        time.sleep(3)  # Keep browser open for a short period to observe the result
    finally:
        driver.quit()
