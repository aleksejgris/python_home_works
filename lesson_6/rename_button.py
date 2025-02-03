from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome (service=ChromeService( ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

abc = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
abc.send_keys("SkyPro")
cba = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

bca = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
print(bca.text)

driver.quit()
