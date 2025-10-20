
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time, random, string

BASE_URL = "http://127.0.0.1:8000"

def build_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Uncomment next line to run headless:
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def test_ambulance_request_form():
    driver = build_driver()
    wait = WebDriverWait(driver, 15)

    try:
        url = f"{BASE_URL}/doctors/ambulance/"
        print("Opening:", url)
        driver.get(url)

        # Wait for form fields
        name_input = wait.until(EC.presence_of_element_located((By.NAME, "name")))
        phone_input = driver.find_element(By.NAME, "phone_number")
        location_input = driver.find_element(By.NAME, "location")
        message_input = driver.find_element(By.NAME, "message")
        urgency_input = driver.find_element(By.NAME, "urgency")

        # Fill the form with random data
        rand = ''.join(random.choices(string.ascii_lowercase, k=4))
        name_input.send_keys(f"Test User {rand}")
        phone_input.send_keys(f"017{random.randint(10000000, 99999999)}")
        location_input.send_keys("Test Location")
        message_input.send_keys("Testing ambulance request form")
        urgency_input.send_keys("High")

        # Submit button
        submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_btn.click()
        print("Submitted ambulance request form")

        # Wait for success page or success text
        wait.until(EC.url_contains("request_success"))
        print("✅ Ambulance request test passed! Redirected to success page.")

    except Exception as e:
        print("❌ Ambulance request test failed:", e)
    finally:
        time.sleep(1)
        driver.quit()

if __name__ == "__main__":
    test_ambulance_request_form()
