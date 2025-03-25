import pytest
from selenium import webdriver
from calculator.Calculator import Calculator

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calculator(driver):
   enter_calculator = Calculator(driver):
   enter_calculator.open()
   enter_calculator.enter()
