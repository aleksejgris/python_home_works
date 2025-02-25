from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
#from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from test_swag_form.login_page.Login import Login
from test_swag_form.overeiw_page.Login import Overeiw
from test_swag_form.cart_page.Cart import Cart
from test_swag_form.inventory_page.Inventory import Inventory
from test_swag_form.checkout_page.Checkout import Checkout

def swag_labs():
 browser= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
 s = Login(browser)
 s.login_page()
 o = Overeiw(browser)
 o.overiew()
 c = Cart(browser)
 c.Cart()
 i = Inventory(browser)
 i.Inventory()
 ch = Checkout(browser)
 ch.Checkout()

 browser.quit()