import allure
from data import Url
from pages.order_feed_page import OrderFeedPage
from selenium.webdriver.common.by import By

@allure.feature('Тесты на проверку раздела "Лента заказов"')
class TestOrderFeed:
    @allure.title('увеличения счетчика "Выполнено за все время" при создании нового заказа')
    def test_check_increment_counter_completed_for_all_time_when_creating_order(self, driver, personal_account, constructor):
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        page = OrderFeedPage(driver)
        personal_account.authorization()
        page.go_to_order_feed()
        counter_before_order = page.get_text_from_counter_completed_for_all_time()
        constructor.go_to_constructor()
        constructor.create_order(driver)
        constructor.close_window_order_id()
        page.go_to_order_feed()
        counter_after_order = page.get_text_from_counter_completed_for_all_time()
        assert counter_after_order > counter_before_order

    @allure.title('увеличения счетчика "Выполнено за сегодня" при создании нового заказа')
    def test_check_increment_counter_completed_for_today_when_creating_order(self, driver, personal_account, constructor):
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        page = OrderFeedPage(driver)
        personal_account.authorization()
        page.go_to_order_feed()
        counter_before_order = page.get_text_from_counter_completed_for_today()
        constructor.go_to_constructor()
        constructor.create_order(driver)
        constructor.close_window_order_id()
        page.go_to_order_feed()
        counter_after_order = page.get_text_from_counter_completed_for_today()
        assert counter_after_order > counter_before_order

    
    @allure.step('Появление заказа в разделе "В работе" после его оформления')
    def test_check_show_order_in_work_when_creating_order(self, driver, personal_account, constructor):
     driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
     personal_account.authorization()
     constructor.create_order(driver)
     order_id = constructor.wait_for_id_to_change()
     constructor.close_window_order_id()
     page = OrderFeedPage(driver)
     page.go_to_order_feed()
     order_id_in_work = page.wait_for_text_in_work_to_change()
     assert order_id == order_id_in_work