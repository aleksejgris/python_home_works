import pytest
from selenium import webdriver
from calculator.Calculator import Calculator
import allure

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка калькулятора")
@allure.description("Введение чисел ,сложения чисел,получения нужного результата")
@allure.feature("READ")
@allure.severity("BLOCKER")
def test_calculator(driver):
    enter_calculator = Calculator(driver)
    with allure.step("Открыть калькулятор"):
      enter_calculator.open()
    with allure.step("Ввести данные в калькулятор и получить результат"):
      enter_calculator.enter()