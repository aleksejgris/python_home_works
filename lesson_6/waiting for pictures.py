from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
driver.maximize_window()
uploaded = WebDriverWait(driver,20)
uploaded.until(
    EC.text_to_be_present_in_elment((By.CSS_SELECTOR,'text'),"Done !")
)
scr = driver.find_element(By.CSS_SELECTOR,'#award').get_attribute('scr')

print(scr)

driver.quit()
