from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_calculator.Calculator import Calculator


def calculator_examination():
    browser= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    b = Calculator(browser)
    b.calculator_expectation()
    b.calculator_enter()
    browser.quit()