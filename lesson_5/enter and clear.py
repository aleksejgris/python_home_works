from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import FireFoxDriverManager

driver = webdriver.FireFox (service=FireFoxService( FireFoxDriverManagerDriver().install()))

driver.get("http://the-internet.herokuapp.com/inputs")
abcd = driver.find_element(By.CSS_SELECTOR,'input[type="number"]')

abcd.send_keys("1000")
abcd.clear()
abcd.send_keys("999")

sleep(5)
