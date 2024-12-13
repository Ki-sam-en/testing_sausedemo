from selenium.webdriver.common.by import By


def test_login_auth(driver):

    username_element = driver.find_element(By.ID, "user-name").send_keys("standard_user")
    password_element = driver.find_element(By.ID, "password").send_keys("secret_sauce")
    submit_element = driver.find_element(By.ID, "login-button").click()

    print("Удалось залогиниться")

    assert "https://www.saucedemo.com/v1/inventory.html" == driver.current_url