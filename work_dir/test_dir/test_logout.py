from selenium.webdriver.common.by import By

def test_logout(driver):

    username_element = driver.find_element(By.ID, "user-name").send_keys("standard_user")
    password_element = driver.find_element(By.ID, "password").send_keys("secret_sauce")
    submit_element = driver.find_element(By.ID, "login-button").click()

    print("Удалось залогиниться")
    
    username_element = driver.find_element(By.CLASS_NAME, "bm-burger-button").click()
    driver.implicitly_wait(3.0)
    password_element = driver.find_element(By.ID, "logout_sidebar_link").click()

    print("Удалось разлогиниться")
    
    assert "https://www.saucedemo.com/v1/index.html" == driver.current_url