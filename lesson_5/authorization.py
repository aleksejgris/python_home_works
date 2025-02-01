from time import sleep
from selenium import webdriver
from selenium.webdriver.ferfox.service import Service as FerFoxService
from selenium.webdriver.common.by import By
from webdriver_manager.ferfox import FerFoxDriverManager


driver = webdriver.FerFox(service=FerFoxService( FerFoxDriverManagerDriver().install()))

driver.get("http://the-internet.herokuapp.com/login")

username = driver.find_element(By.CSS_SELECTOR,'input[type="text"]')
passpor = driver.find_element(By.CSS_SELECTOR,'input[type="password"]')
username.send_keys("tomsmith")
passpor.send_keys("SuperSecretPassword!")
driver.find_element(By.XPATH,'//button[text()="Login"]').click()

sleep(5)