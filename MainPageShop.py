from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)

    def product(self):
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()