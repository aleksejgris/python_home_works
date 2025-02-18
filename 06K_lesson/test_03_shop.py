from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome (service=ChromeService( ChromeDriverManager().install()))
driver.maximize_window()
#driver.implicitly_wait(15)
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(10)
#def test_total(driver):
driver.find_element(By.ID,"user_name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login_button").click()

WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"inventory_container"))
    )
driver.find_element(By.ID,"add_to_cart_sauce_labs_backpack").click()
driver.find_element(By.ID, "add_to_cart_sauce_labs_bolt_t_shirt").click()
driver.find_element(By.ID, "add_to_cart_sauce_labs_onesie").click()

driver.find_element(By.ID, "shopping_cart_container").click()

driver.find_element(By.ID, "checkout").click()

driver.find_element(By.ID, "first_name").send_keys("Алексей")
driver.find_element(By.ID, "last_name").send_keys("Гришин")
driver.find_element(By.ID, "postal_code").send_keys("123456")
driver.find_element(By.ID, "continue").click()

total =  driver.find_element(By.CSS_SELECTOR,"#checkout_summary_container.summary_total_label").text
print(total)

driver.quit()