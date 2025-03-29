from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator:

    def __inint__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
            self.driver.get(
                "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )


    def enter(self):
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()
        self.driver.implicitly_wait(47)