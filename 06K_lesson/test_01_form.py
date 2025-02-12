from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome (service=ChromeService( ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
wait = WebDriverWait(driver, 20)  # ожидание до 10 секунд
first_name_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#first_name")))
first_name_field.send_keys("Иван")

#driver.find_element(By.CSS_SELECTOR,"#first_name").send_keys("Иван")
driver.find_element(By.CSS_SELECTOR,"#last_name").send_keys("Петров")
driver.find_element(By.CSS_SELECTOR,"#address").send_keys("Ленина,55-3")
driver.find_element(By.CSS_SELECTOR,"#e_mail").send_keys("test@skypro.com")
driver.find_element(By.CSS_SELECTOR,"#phone").send_keys("+7985899998787")
driver.find_element(By.CSS_SELECTOR,"#city").send_keys("Москва")
driver.find_element(By.CSS_SELECTOR,"#country").send_keys("Россия")
driver.find_element(By.CSS_SELECTOR,"#job_position").send_keys("QA")
driver.find_element(By.CSS_SELECTOR,"#company").send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR,"button[type='Submit']").click()

waiter = WebDriverWait(driver,40)

alert_danger_color = "rgba(248,215,218,1)"
zip_code = driver.find_element(By.CSS_SELECTOR,"#zip_code")
color_zip = zip_code.value_of_css_property("background-color")
assert color_zip == alert_danger_color,f"Expected {alert_danger_color}, but got{color_zip}"

fields = ["first_name","last_name","address","e_mail","phone","country","job_position","company"]
for field in fields:
    element = driver.find_element(By.ID,field)
    color = element.value_of_css_property("background-color")
    assert color == "rgba(209,231,221,1)", f"Field{field} is not highlighted in green"

    driver.quit()
