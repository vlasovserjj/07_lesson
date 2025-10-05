from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.MainPageCalc import MainPage

def test_cart_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    main_page = MainPage(browser)
    main_page.delay_clear()
    main_page.delay_input_field(9)
    main_page.click_to_button('7')
    main_page.click_to_button('+')
    main_page.click_to_button('8')
    main_page.click_to_button('=')
    monitor = main_page.example('15')
    assert monitor == '15'
    browser.quit()