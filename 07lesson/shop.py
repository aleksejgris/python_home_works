from selenium.webdriver.common.by import By

class Shop:

 def shop_entrance(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.implicitly_wait(10)
#def test_total(driver):
 def shop_login(self):
     self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
     self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
     self.driver.find_element(By.ID,"login_button").click()

 def shop_product_selection(self):
     # self.WebDriverWait(driver,10).until(
      #     EC.presence_of_element_located((By.ID,"inventory_container"))        <? не понимаю ?
      #)
     self.driver.find_element(By.ID,"add_to_cart_sauce_labs_backpack").click()
     self.driver.find_element(By.ID, "add_to_cart_sauce_labs_bolt_t_shirt").click()
     self.driver.find_element(By.ID, "add_to_cart_sauce_labs_onesie").click()
     self.driver.find_element(By.ID, "shopping_cart_container").click()

 def shop_checkout(self):
    self.driver.find_element(By.ID, "checkout").click()

 def shop_authorization(self):
    self.driver.find_element(By.ID, "first_name").send_keys("Алексей")
    self.driver.find_element(By.ID, "last_name").send_keys("Гришин")
    self.driver.find_element(By.ID, "postal_code").send_keys("123456")
    self.driver.find_element(By.ID, "continue").click()
 def total_price(self):
    self.driver.find_element(By.CSS_SELECTOR,"#checkout_summary_container.summary_total_label").text
 #print(total)

