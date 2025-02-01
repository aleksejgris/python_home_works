from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome (service=ChromeService( ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
for _ in range(5):
  driver.find_element(By.XPATH, '//button[text()="Add Element"]').click()

add = driver.find_elements(By.XPATH,'//button[text()="Delete"]')
print("Список:",len(add))

sleep(5)


#css selector
#id
#name
#link text
#partial link text
#tag name
#xpath