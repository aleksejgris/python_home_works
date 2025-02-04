from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome (service=ChromeService( ChromeDriverManager().install()))
driver.implicitly_wait(40)
driver.maximize_window()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


abc = driver.find_element(By.CSS_SELECTOR, 'img[scr = "img/award.png"]').text
print(abc)

driver.quit()
