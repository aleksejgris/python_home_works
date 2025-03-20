from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#from selenium.webdriver.firefox.service import Service as FireFoxService
#from webdriver_manager.firefox import GeckoDriverManager


#browser = webdriver.FireFox(service=FireFoxService(GeckoDriverManager().install()))


browser = webdriver.Chrome (service=ChromeService( ChromeDriverManager().install()))
browser.maximize_window()
browser.get("https://ya.ru")
sleep(5)

browser.save_screenshot('./ya_.png')
browser.guit()
