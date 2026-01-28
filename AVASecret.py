from selenium import webdriver
from selenium.webdriver.common.by import By

def chrome_browser():
    driver = webdriver.Chrome()
    return driver

def open_platform(driver):
    driver.get('https://www.testrail.com/')
    element = driver.find_element(By.ID, 'header-navbar')
    # Example interaction: print the text of the navbar
    print(element.text)
    # You can add additional interactions here, such as clicking a link inside the navbar if needed

# Example usage
if __name__ == '__main__':
    driver = chrome_browser()
    try:
        open_platform(driver)
    finally:
        driver.quit()
