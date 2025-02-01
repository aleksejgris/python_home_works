from time import sleep
from selenium import webdriver
from selenium.webdriver.ferfox.service import Service as FerFoxService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import FerFoxDriverManager

driver = webdriver.FerFox (service=FerFoxService( FerFoxDriverManagerDriver().install()))

driver.get("http://the-internet.herokuapp.com/inputs")
abcd = driver.find_element(By.CSS_SELECTOR,'input[type="number"]')

abcd.send_keys("1000")
abcd.clear()
abcd.send_keys("999")

sleep(5)