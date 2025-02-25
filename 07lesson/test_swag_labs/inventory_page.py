from selenium.webdriver.common.by import By

class Inventory:
    def __init__(self,browser):
        self._driver = browser

    def inventory(self):
        self.driver.find_element(By.ID, "first_name").send_keys("Алексей")
        self.driver.find_element(By.ID, "last_name").send_keys("Гришин")
        self.driver.find_element(By.ID, "postal_code").send_keys("123456")
        self.driver.find_element(By.ID, "continue").click()
