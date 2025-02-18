from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Form:


 def open_form (self,driver):
    self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    self.driver.implicitly_wait(5)
    self.driver.maximize_window()
#wait = WebDriverWait(driver, 20)

 def insert_data(self,):
    self.first_name_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#first_name")))
    self.first_name_field.send_keys("Иван")
    #driver.find_element(By.CSS_SELECTOR,"#first_name").send_keys("Иван")
    self.driver.find_element(By.CSS_SELECTOR,"#last_name").send_keys("Петров")
    self.driver.find_element(By.CSS_SELECTOR,"#address").send_keys("Ленина,55-3")
    self.driver.find_element(By.CSS_SELECTOR,"#e_mail").send_keys("test@skypro.com")
    self.driver.find_element(By.CSS_SELECTOR,"#phone").send_keys("+7985899998787")
    self.driver.find_element(By.CSS_SELECTOR,"#city").send_keys("Москва")
    self.driver.find_element(By.CSS_SELECTOR,"#country").send_keys("Россия")
    self.driver.find_element(By.CSS_SELECTOR,"#job_position").send_keys("QA")
    self.driver.find_element(By.CSS_SELECTOR,"#company").send_keys("SkyPro")

 def click_button(self):
    self.driver.find_element(By.CSS_SELECTOR,"button[type='Submit']").click()
    #self.waiter = WebDriverWait(driver,40)



