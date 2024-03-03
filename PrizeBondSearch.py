import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.bb.org.bd/en/index.php/Investfacility/prizebond')
driver.maximize_window()

with open(r'D:\Pycharm\Project\Prize bond search tool\Prize bond.txt', 'r') as file:
    search_query = file.read().strip()

# Locate the search box element (replace 'searchbox_id' with the actual ID of the search box)
search_box = driver.find_element(By.ID, 'gsearch')
# Enter the search string
search_box.send_keys(search_query)
# Locate the search button element (replace 'search_button_id' with the actual ID of the search button)
search_button = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section/div/div/div[2]/div/div/span/div[2]/form/button')
# Click the search button
search_button.click()
response = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section/div/div/div[2]/div/div/span/font[2]')
response_text = response.text
print(response_text)
if "No Match Found" in response_text:
    driver.quit()
else:
    time.sleep(60)