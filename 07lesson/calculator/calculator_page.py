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
        self.browser.find_element(By.XPATH, '//span[text()="7"]').click()
        self.browser.find_element(By.XPATH, '//span[text()="+"]').click()
        self.browser.find_element(By.XPATH, '//span[text()="8"]').click()
        self.browser.find_element(By.XPATH, '//span[text()="="]').click()
        self.browser.implicitly_wait(47)

# WebDriverWait(driver, 45).until(
 #       EC.text_to_be_present_in_element(By.CSS_SELECTOR, ["#screen"]), '15')

# result = driver.find_element(By.CSS_SELECTOR, "#screen").text
 #assert int(result) == 15
