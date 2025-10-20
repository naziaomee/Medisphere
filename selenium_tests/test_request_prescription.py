from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os, time, random, string

# Optional: allow running visible browser by setting SHOW_BROWSER=1
SHOW_BROWSER = os.environ.get("SHOW_BROWSER", "") == "1"

def build_driver():
    options = webdriver.ChromeOptions()
    if not SHOW_BROWSER:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1440,900")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def test_request_prescription_page_and_submit():
    driver = build_driver()
    try:
        base_url = os.environ.get("BASE_URL", "http://127.0.0.1:8000")
        url = base_url.rstrip("/") + "/doctors/request_prescription/"
        driver.get(url)

        # Small wait and print page source for debugging
        time.sleep(2)
        print("🔹 Current URL:", driver.current_url)
        print("🔹 Page snippet:\n", driver.page_source[:1000])

        wait = WebDriverWait(driver, 10)

        # Try to locate the form
        forms = driver.find_elements(By.TAG_NAME, "form")
        if not forms:
            print("❌ No form found on page!")
            return
        form = forms[0]
        print("✅ Form found!")

        # Fill all input fields dynamically
        for input_el in form.find_elements(By.TAG_NAME, "input"):
            type_attr = input_el.get_attribute("type")
            if type_attr in ["text", "email", "tel"]:
                input_el.clear()
                input_el.send_keys("Test " + ''.join(random.choices(string.ascii_letters, k=4)))
            elif type_attr == "number":
                input_el.clear()
                input_el.send_keys(str(random.randint(1, 100)))
            elif type_attr == "password":
                input_el.clear()
                input_el.send_keys("Testpass123!")

        for textarea in form.find_elements(By.TAG_NAME, "textarea"):
            textarea.clear()
            textarea.send_keys("This is a test prescription note.")

        for select in form.find_elements(By.TAG_NAME, "select"):
            options = select.find_elements(By.TAG_NAME, "option")
            if options:
                options[1].click()  # select second option

        # Submit the form
        submit_btn = form.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_btn.click()
        print("🔹 Form submitted, waiting for success message...")

        # Wait for success keywords in page
        success_keywords = ["success", "thank", "submitted", "requested", "dashboard"]
        WebDriverWait(driver, 10).until(
            lambda d: any(k in d.page_source.lower() for k in success_keywords)
        )
        print("✅ Prescription request form submitted successfully!")

    finally:
        if SHOW_BROWSER:
            time.sleep(2)
        driver.quit()

# Run the test directly
if __name__ == "__main__":
    test_request_prescription_page_and_submit()
