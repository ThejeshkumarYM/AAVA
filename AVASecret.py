from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, TimeoutException
import traceback
import sys
import time

print("Thejesh Script Started")

def create_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)

def test_testrail(driver):
    driver.get("https://www.testrail.com/")
    time.sleep(5)

    if "TestRail" not in driver.title:
        raise Exception(f"Unexpected page title: {driver.title}")

    print("✅ TestRail page loaded successfully")
    print("Title:", driver.title)

try:
    driver = create_driver()

    test_testrail(driver)

    print("✅ OVERALL STATUS : PASSED")

except Exception as e:
    print("❌ OVERALL STATUS : FAILED")
    print("❌ ERROR:", str(e))
    traceback.print_exc()

    try:
        driver.save_screenshot("failure.png")
        print("Screenshot saved")
    except:
        pass

    sys.exit(1)

finally:
    try:
        driver.quit()
    except:
        pass
