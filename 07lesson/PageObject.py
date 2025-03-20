#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait

#from form import Form
#from calc import Calc
#from shop import Shop

#def form_test():
 #   driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  #  a = Form(driver)
   # a.open_form()
    #a.insert_data()
   # a.click_button()

    #alert_danger_color = "rgba(248,215,218,1)"
    #zip_code = driver.find_element(By.CSS_SELECTOR,"#zip_code")
    #color_zip = zip_code.value_of_css_property("background-color")
    #assert color_zip == alert_danger_color,f"Expected {alert_danger_color}, but got{color_zip}"

    #fields = ["first_name","last_name","address","e_mail","phone","country","job_position","company"]
    #for field in fields:
    #element = driver.find_element(By.ID,field)
    #color = element.value_of_css_property("background-color")
    #assert color == "rgba(209,231,221,1)", f"Field{field} is not highlighted in green"
   # driver.quit()

#def calc_test():
 #   driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  #  b = Calc(driver)
  #  b.calc_expectation()
   # b.calc_enter()
    #WebDriverWait(driver, 45).until(
     #EC.text_to_be_present_in_element(By.CSS_SELECTOR,["#screen"]),'15')

   # result = driver.find_element(By.CSS_SELECTOR,"#screen").text
   # assert int(result) == 15
   # driver.quit()

#def shop_test():
 #   driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  #  c = Shop(driver)
   # c.shop_entrance()
   # c.shop_login()
    #c.shop_product_selection()
    #c.shop_checkout()
    #c.shop_authorization()
    #c.total_price()
    #driver.quit()