from selenium.webdriver.common.by import By

class Order:
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)

    def first_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(term)
    
    def last_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(term)

    def postal_code(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(term)

    def continue_click(self):
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()


    def sum(self):
        self._driver.find_element(By.CLASS_NAME, "summary_total_label").text

    def sum(self):
        price = self._driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return price