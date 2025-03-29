import allure
import pytest
from selenium import webdriver
from pages.FormPage import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature('CREATE')
@allure.title('Авторизация на сайте')
@allure.description('Заполнения формы,'
                    'проверка цвета заполненых блоков,'
                    'проверка отправки заполненой формы')
@allure.severity('blocker')
def test_form_submission_flow(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form()
    form_page.submit_form()
    form_page.check_form_submission()