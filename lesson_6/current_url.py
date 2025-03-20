from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome (service=ChromeService( ChromeDriverManager().install()))
browser.get("https://ya.ru")
url = browser.current_url()
print(url)
browser.guit()