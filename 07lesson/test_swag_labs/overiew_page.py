from selenium.webdriver.common.by import By

class Overeiw:
    def __init__ (self,browser):
        self._driver = browser

    def overiew(self):
        self.driver.find_element(By.ID, "add_to_cart_sauce_labs_backpack").click()
        self.driver.find_element(By.ID, "add_to_cart_sauce_labs_bolt_t_shirt").click()
        self.driver.find_element(By.ID, "add_to_cart_sauce_labs_onesie").click()
        self.driver.find_element(By.ID, "shopping_cart_container").click()