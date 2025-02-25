import f
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from test_data_form.base_page.Basa_page import Basa_page

def field_checking():
 browser= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
 f = Basa_page(browser)
 f.open_form
 f.insert_data
 f.click_button


 f.quit()