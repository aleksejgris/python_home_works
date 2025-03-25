from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome (service=ChromeService( ChromeDriverManager().install()))
browser.get("https://ya.ru")

current_title = browser.title
print(current_title)
browser.guit()