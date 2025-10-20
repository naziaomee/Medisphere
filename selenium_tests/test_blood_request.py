# test_blood_request.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# --- CONFIG ---
BLOOD_REQUEST_URL = "http://127.0.0.1:8000/doctors/blood-request/"
SUCCESS_URL = "http://127.0.0.1:8000/doctors/blood-request-success/"

# Example data to submit
BLOOD_TYPE = "A+"
QUANTITY = "5"
HOSPITAL_NAME = "City Hospital"
CONTACT_INFO = "0123456789"

def build_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def test_blood_request():
    driver = build_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(BLOOD_REQUEST_URL)
        print(f"🔹 Opened blood request page: {driver.current_url}")

        # Fill blood type select field
        blood_type_select = Select(wait.until(EC.presence_of_element_located((By.NAME, "blood_type"))))
        blood_type_select.select_by_value(BLOOD_TYPE)

        # Fill quantity
        quantity_input = wait.until(EC.presence_of_element_located((By.NAME, "quantity")))
        quantity_input.clear()
        quantity_input.send_keys(QUANTITY)

        # Fill hospital name
        hospital_input = wait.until(EC.presence_of_element_located((By.NAME, "hospital_name")))
        hospital_input.clear()
        hospital_input.send_keys(HOSPITAL_NAME)

        # Fill contact info
        contact_input = wait.until(EC.presence_of_element_located((By.NAME, "contact_info")))
        contact_input.clear()
        contact_input.send_keys(CONTACT_INFO)

        # Submit the form
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit_button.click()
        print("🔹 Submitted blood request form.")

        # Wait for redirect to success page
        wait.until(EC.url_to_be(SUCCESS_URL))
        print("✅ Blood request successful! Redirected to success page.")

    except Exception as e:
        print(f"❌ Blood request test failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_blood_request()
