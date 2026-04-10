from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_sauce_demo():
    # Simplest way to open Chrome in modern Selenium
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    try:
        # TEST 1: Locked Out User
        print("Starting Locked Out User Test...")
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        error_msg = driver.find_element(By.TAG_NAME, "h3").text
        assert "locked out" in error_msg
        print("PASS: Locked out user blocked correctly.")

        # TEST 2: Valid Purchase
        print("Starting Standard User Purchase Flow...")
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").clear()
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Add item and checkout
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        # Fill info (Your name)
        driver.find_element(By.ID, "first-name").send_keys("Kalluru")
        driver.find_element(By.ID, "last-name").send_keys("Badulla")
        driver.find_element(By.ID, "postal-code").send_keys("522237")
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()

        assert "checkout-complete" in driver.current_url
        print("PASS: Purchase completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    test_sauce_demo()