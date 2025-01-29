from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome (service=ChromeService( ChromeDriverManager().install()))
driver.implicitly_wait(20)

driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR,"#ajaxButton").click()
cba = driver.find_element(By.CSS_SELECTOR,"#content")
abc = cba.find_element(By.CSS_SELECTOR,"#p.bg_success").text
print(abc)

driver.guit()