from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Calc:

 def calc_expectation(self):
    self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    self.driver.maximize_window()
    self.delay_input = driver.find_element(By.ID,"delay")
    self.delay_input.clear()
    self.delay_input.send_keys("45")

 def calc_enter(self):
    self.driver.find_element(By.XPATH,'//span[text()="7"]').click()
    self.driver.find_element(By.XPATH,'//span[text()="+"]').click()
    self.driver.find_element(By.XPATH,'//span[text()="8"]').click()
    self.driver.find_element(By.XPATH,'//span[text()="="]').click()
    self.driver.implicitly_wait(5)

#WebDriverWait(driver,45).until(
    #EC.text_to_be_present_in_element(By.CSS_SELECTOR,["#screen"]),'15')

#result = driver.find_element(By.CSS_SELECTOR,"#screen").text
#assert int(result) == 15

