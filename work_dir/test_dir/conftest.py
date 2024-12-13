# файл, в котором я буду определять фикстуры. его не нужно импортировать
# так как делает это pytest

import pytest
from selenium import webdriver
import allure

@pytest.fixture(autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(autouse=True)
@allure.title("выбор браузера")
def driver(browser):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        print("Выбран Chrome")
        driver.get("http://www.saucedemo.com/v1")

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        print("Выбран Firefox")
        driver.get("http://www.saucedemo.com/v1")
        
    else:
        print("Браузер не выбран")

    yield driver

    with allure.step("Доступ к сайту"):  
        print("Завершение сессии")

    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", action="store")
