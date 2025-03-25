from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import FireFoxDriverManager

driver = webdriver.FireFox (service=FireFoxService( FireFoxDriverManagerDriver().install()))

driver.get("http://the-internet.herokuapp.com/entry_ad")
driver.find_element(By.CSS_SELECTOR, 'div.modal-footer > p').click()

sleep(5)
