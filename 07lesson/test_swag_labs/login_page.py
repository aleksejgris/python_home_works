from selenium.webdriver.common.by import By

class Login:
    def login_page(self,browser):
        self.browser.get("https://www.saucedemo.com/")
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.ID, "user-name").send_keys("standard_user")
        self.browser.find_element(By.ID, "password").send_keys("secret_sauce")
        self.browser.find_element(By.ID, "login_button").click()