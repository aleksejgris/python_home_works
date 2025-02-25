from selenium.webdriver.common.by import By

class Cart:
    def __int__(self,browser):
        self._driver = browser

    def cart(self):
        self.driver.find_element(By.ID, "checkout").click()