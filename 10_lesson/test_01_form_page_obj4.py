import pytest
from selenium import webdriver
from pages.FormPage import FormPage
import allure

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка авторизации заполненой формы ")
@allure.description("Заполнения формы данными,проверка отображения цвета заполненых и не заполненых строчек,"
                    "отправка заполненой формы")
@allure.feature("READ")
@allure.severity("BLOCKER")
def test_form_submission_flow(driver):
    form_page = FormPage(driver)
    with allure.step("Открыть страницу заполнения формы"):
     form_page.open()
    with allure.step("Заполнить форму"):
     form_page.fill_form()
    with allure.step("Нажать кнопку <submit> c заполненой формой"):
     form_page.submit_form()
    with allure.step("Проверить результат отправки формы"):
     form_page.check_form_submission()