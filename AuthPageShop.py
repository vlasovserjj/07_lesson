from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Auth:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def user_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(term)

    def password(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(term)
    
    def click_login(self):
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()