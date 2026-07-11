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
    time.sleep(5)

    if "TestRail" in driver.title:
        print("✅ Status Report: SUCCESS")
        print("URL: https://www.testrail.com/")
        print("Title:", driver.title)
    else:
        raise Exception(f"Unexpected page title: {driver.title}")

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
