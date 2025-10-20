# test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# --- CONFIG ---
LOGIN_URL = "http://127.0.0.1:8000/doctors/login_doctor/"
DOCTOR_EMAIL = "omeenazia@gmail.com"
DOCTOR_PASSWORD = "yourpassword"
#DASHBOARD_URL = "http://127.0.0.1:8000/doctors/doctor_dashboard/"

def build_driver():
    """Setup Chrome driver"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def test_doctor_login():
    driver = build_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(LOGIN_URL)
        print(f"🔹 Opened login page: {driver.current_url}")

        # Wait for email field
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))

        # Fill in credentials
        email_input.clear()
        email_input.send_keys(DOCTOR_EMAIL)
        password_input.clear()
        password_input.send_keys(DOCTOR_PASSWORD)

        # Submit the form
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit_button.click()
        print("🔹 Submitted login form.")

        # Wait for dashboard
        wait.until(EC.url_to_be(DASHBOARD_URL))
        print("✅ Login successful! Redirected to dashboard.")

    except Exception as e:
        print(f"❌ Login test failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_doctor_login()
