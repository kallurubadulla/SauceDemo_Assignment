import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    # Setup
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    # Teardown
    driver.quit()

def test_login_and_checkout(driver):
    login_page = LoginPage(driver)
    
    # 1. Open Site
    driver.get("https://www.saucedemo.com")
    
    # 2. Login using the Page Object
    login_page.login("standard_user", "secret_sauce")
    
    # 3. Verify Login Success
    assert "inventory.html" in driver.current_url
    print("PASS: Login successful.")
