#test_blog_crud.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time, random, string

# Helper function to generate random strings for titles
def random_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 10)

BASE_URL = "http://127.0.0.1:8000/doctors/health/"

try:
    # 1️⃣ Create a new blog post
    driver.get(BASE_URL)
    wait.until(EC.presence_of_element_located((By.NAME, 'title')))
    
    title_input = driver.find_element(By.NAME, 'title')
    content_input = driver.find_element(By.NAME, 'content')
    
    new_title = "Selenium Blog " + random_string()
    title_input.send_keys(new_title)
    content_input.send_keys("This is content created by Selenium.")

    # Click the Create Post button
    create_button = driver.find_element(By.XPATH, "//button[contains(text(),'Create Post')]")
    create_button.click()
    
    time.sleep(2)  # wait for page reload / redirect

    # 2️⃣ Verify post creation
    assert new_title in driver.page_source
    print("✅ Blog post created successfully")

    # 3️⃣ Update the blog post
    edit_link = driver.find_element(By.LINK_TEXT, "Edit")  # Your edit link text is "Edit"
    edit_link.click()
    
    wait.until(EC.presence_of_element_located((By.NAME, 'title')))
    title_input = driver.find_element(By.NAME, 'title')
    title_input.clear()
    updated_title = new_title + " Updated"
    title_input.send_keys(updated_title)
    
    update_button = driver.find_element(By.XPATH, "//button[contains(text(),'Create Post')]")  # The same submit button
    update_button.click()
    
    time.sleep(2)
    assert updated_title in driver.page_source
    print("✅ Blog post updated successfully")

    # 4️⃣ Delete the blog post
    delete_link = driver.find_element(By.LINK_TEXT, "Delete")  # Your delete link text
    delete_link.click()
    
    time.sleep(2)
    assert updated_title not in driver.page_source
    print("✅ Blog post deleted successfully")

finally:
    driver.quit()
