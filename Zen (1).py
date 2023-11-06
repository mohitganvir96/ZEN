#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

def date_selector(driver, inptdate):
    startdate, enddate = map(int, inptdate.split('-'))

    while startdate <= enddate:
        textstring = str(startdate) + "\\" + str(startdate + 1)
        print(textstring)
        driver.find_element(By.XPATH, "//select[@name='season_id']/option[text()='" + textstring + "']").click()
        startdate += 1

    # Rest of your code...

# Replace 'path_to_chromedriver' with the path to your ChromeDriver executable.
driver_path = 'C:/Users/Lenovo/Downloads/chromedriver_win64/chromedriver_win64/chromedriver.exe'
service = ChromeService(executable_path=driver_path)
options = Options()
options.headless = False  # Set to True if you want to run the browser in headless mode.
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://windscribe.com/")
# Wait for the login form to load using a CSS selector
login_form_locator = (By.CSS_SELECTOR, "#loginform")  # Updated CSS selector for login form
wait = WebDriverWait(driver, 40)
try:
    login_form = wait.until(EC.visibility_of_element_located(login_form_locator))
except TimeoutException as e:
    print("TimeoutException occurred while waiting for login form")
    print(str(e))
    driver.save_screenshot("timeout.png")
    driver.quit()
    exit()

# Call the date_selector function and pass the date input
inptdate = '1-5'  # Example date input
date_selector(driver, inptdate)

# Log in with the provided credentials
username = "lavender1033"
password = "lavender1033"

username_input = driver.find_element(By.CLASS_NAME, "username")  # Assuming the input field has a class name "username"
password_input = driver.find_element(By.CLASS_NAME, "password")  # Assuming the input field has a class name "password"

username_input.send_keys(username)
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

# Wait for the Features link to be clickable using CSS_SELECTOR
features_link = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/features']")))
features_link.click()

# Locate the General Features section and scrape feature names using CSS_SELECTOR
general_features_section = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2:contains('General Features')")))
general_features_names = general_features_section.find_elements(By.CSS_SELECTOR, "ul li")

# Extract and print feature names
feature_names = [feature.text for feature in general_features_names]
print("General Features:")
print("\n".join(feature_names))

# Rest of your code...

# Close the browser window
driver.quit()


# In[ ]:




