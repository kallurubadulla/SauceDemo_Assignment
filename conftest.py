import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    """
    Setup: This runs before every test function.
    It initializes the browser and sets the environment.
    """
    print("\nInitializing Chrome Browser...")
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Uncomment to run without opening a window
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    yield driver # This is where the actual test script "plugs in" and runs
    
    """
    Teardown: This runs after the test is finished.
    """
    print("\nClosing Browser...")
    driver.quit()