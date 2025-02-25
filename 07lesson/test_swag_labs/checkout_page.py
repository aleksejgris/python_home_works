from selenium.webdriver.common.by import By


class Checkout:
    def __init__(self, browser):
     self._driver = browser

    def checkout(self):
     self.driver.find_element(By.CSS_SELECTOR, "#checkout_summary_container.summary_total_label").text
