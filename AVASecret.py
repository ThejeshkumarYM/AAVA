from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, TimeoutException
import traceback
import time

print("Thejesh Script Started")

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
    driver.get("https://www.testrail.com/")
    time.sleep(10)

    print("Current URL:", driver.current_url)
    print("Page Title:", driver.title)

    print("Page Source Preview:")
    print(driver.page_source[:1000])

try:
    driver = create_driver()

    test_google(driver)
    test_testrail(driver)

    print("✅ OVERALL STATUS : PASSED")

except Exception as e:
    print("❌ OVERALL STATUS : FAILED")
    print("❌ ERROR :", str(e))
    traceback.print_exc()

    try:
        driver.save_screenshot("failure.png")
    except:
        pass

    raise

finally:
    try:
        driver.quit()
    except:
        pass
