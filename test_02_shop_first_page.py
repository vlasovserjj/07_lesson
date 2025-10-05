from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.AuthPageShop import Auth
from pages.MainPageShop import MainPage
from pages.CartPageShop import Cart
from pages.OrderPageShop import Order

def test_cart_counter():
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    auth_page = Auth(browser)
    #логин: standard_user
    auth_page.user_name("standard_user")
    #пароль: secret_sauce
    auth_page.password("secret_sauce")
    #нажать "login"
    auth_page.click_login()



    #ввести локатор продукта
    #добавить 3 продукта
    main_page = MainPage(browser)
    main_page.product()
    main_page.go_to_cart()

    cart = Cart(browser)
    cart.click_chek()
    
    buy = Order(browser)
    buy.first_name("Сергей")
    buy.last_name("Иванов")
    buy.postal_code("412275")
    buy.continue_click()
    total_price = buy.sum()
    browser.quit()
    expected = "Total: $58.29"
    assert total_price == expected