
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome (service=ChromeService( ChromeDriverManager().install()))

cookie = {
    'name':'cookie_policy',
    'value': '1'
}

browser.get("https://labirint.ru")
browser.add_cookie(cookie)
browser.refresh()

sleep(10)

