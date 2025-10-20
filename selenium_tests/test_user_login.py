# test_user_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- CONFIG ---
LOGIN_URL = "http://127.0.0.1:8000/doctors/login/"
USER_EMAIL = "omeenazia@gmail.com"
USER_PASSWORD = "yourpassword"

def build_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def test_user_login():
    driver = build_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(LOGIN_URL)
        print(f"🔹 Opened user login page: {driver.current_url}")

        # Wait for username and password fields
        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))

        # Fill credentials
        print(f"🔹 Typing username/email: {USER_EMAIL}")
        username_input.clear()
        username_input.send_keys(USER_EMAIL)

        print(f"🔹 Typing password: {'*' * len(USER_PASSWORD)} (masked in browser)")
        password_input.clear()
        password_input.send_keys(USER_PASSWORD)

        time.sleep(1)  # small pause to see typing

        # Submit the form
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        print("🔹 Clicking login button...")
        submit_button.click()

        # Optional: wait a bit to see the result page
        time.sleep(3)
        print("✅ User login test completed (no redirect check).")

    except Exception as e:
        print(f"❌ User login test failed: {e}")
        time.sleep(5)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_user_login()
