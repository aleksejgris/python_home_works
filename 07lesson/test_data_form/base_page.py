from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Basa_page:

 def open_form (self,browser):
    self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    self.browser.implicitly_wait(5)
    self.browser.maximize_window()
#wait = WebDriverWait(driver, 20)

 def insert_data(self,):
    self.first_name_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#first_name")))
    self.first_name_field.send_keys("Иван")
    self.browser.find_element(By.CSS_SELECTOR,"#first_name").send_keys("Иван")
    self.browser.find_element(By.CSS_SELECTOR,"#last_name").send_keys("Петров")
    self.browser.find_element(By.CSS_SELECTOR,"#address").send_keys("Ленина,55-3")
    self.browser.find_element(By.CSS_SELECTOR,"#e_mail").send_keys("test@skypro.com")
    self.browser.find_element(By.CSS_SELECTOR,"#phone").send_keys("+7985899998787")
    self.browser.find_element(By.CSS_SELECTOR,"#city").send_keys("Москва")
    self.browser.find_element(By.CSS_SELECTOR,"#country").send_keys("Россия")
    self.browser.find_element(By.CSS_SELECTOR,"#job_position").send_keys("QA")
    self.browser.find_element(By.CSS_SELECTOR,"#company").send_keys("SkyPro")

 def click_button(self):
        self.browser.find_element(By.CSS_SELECTOR, "button[type='Submit']").click()
