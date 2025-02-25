from selenium.webdriver.common.by import By
class Calculator:

    def calculator_expectation(self):
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.browser.maximize_window()
        self.delay_input = browser.find_element(By.ID, "delay")
        self.delay_input.clear()
        self.delay_input.send_keys("45")

    def calculator_enter(self):
        self.browser.find_element(By.XPATH, '//span[text()="7"]').click()
        self.browser.find_element(By.XPATH, '//span[text()="+"]').click()
        self.browser.find_element(By.XPATH, '//span[text()="8"]').click()
        self.browser.find_element(By.XPATH, '//span[text()="="]').click()
        self.browser.implicitly_wait(47)

# WebDriverWait(driver, 45).until(
 #       EC.text_to_be_present_in_element(By.CSS_SELECTOR, ["#screen"]), '15')

# result = driver.find_element(By.CSS_SELECTOR, "#screen").text
 #assert int(result) == 15