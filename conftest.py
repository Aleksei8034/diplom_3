import pytest
from selenium import webdriver
import data
from pages.personal_account_page import PersonalAccountPage
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        data.DRIVER_NAME = 'chrome'
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
    else:
        data.DRIVER_NAME = 'firefox'
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


