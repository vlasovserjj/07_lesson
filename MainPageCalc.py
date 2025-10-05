from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    #очистить поле ожидания
    def delay_clear(self):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()

    #ввести число в поле ожидания
    def delay_input_field(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(term)

    #нажать кнопки калькулятора
    def click_to_button(self, term):
        button_locator = "//span[text()='{}']"
        button_to_click = (term)
        self._driver.find_element(By.XPATH, button_locator.format(button_to_click)).click()

    #результат
    def example(self, expected_result):
        waiter = WebDriverWait(self._driver, 50)
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), expected_result))
        return expected_result
    


    