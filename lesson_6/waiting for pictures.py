from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome (service=ChromeService( ChromeDriverManager().install()))
driver.implicitly_wait(20)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
sleep(25)

abc = driver.find_element(By.CSS_SELECTOR, "img/award.png")
print(abc)

driver.guit()