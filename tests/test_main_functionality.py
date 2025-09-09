import pytest
import allure
from data import Url, UserData
from pages.personal_account_page import PersonalAccountPage  
from pages.constructor_page import ConstructorPage          
from pages.order_feed_page import OrderFeedPage            

@allure.feature('Тесты на проверку основного функционала')
class TestMainFunctionality:
    @allure.title('переход на "Конструктор" из формы авторизации')
    def test_check_go_to_constructor_from_personal_account_unauthorized(self, driver):
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account = PersonalAccountPage(driver)
        constructor = ConstructorPage(driver)
        personal_account.go_to_personal_account()
        constructor.go_to_constructor()
        text = constructor.is_constructor_visible().text
        assert text == 'Соберите бургер'

    @allure.title('перехода на "Конструктор" из Личного кабинета')
    def test_check_go_to_constructor_from_personal_account_authorized(self, driver):
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account = PersonalAccountPage(driver)
        constructor = ConstructorPage(driver)
        personal_account.authorization(UserData.email, UserData.password) 
        personal_account.go_to_personal_account()
        constructor.go_to_constructor()
        text = constructor.is_constructor_visible().text
        assert text == 'Соберите бургер'

    @allure.title('переход на "Конструктор" из "Ленты заказов"')
    def test_check_go_to_constructor_from_order_feed(self, driver):
        driver.get(Url.URL_ORDER_FEED)
        constructor = ConstructorPage(driver)
        constructor.go_to_constructor()
        text = constructor.is_constructor_visible().text
        assert text == 'Соберите бургер'

    @allure.title('переход на "Ленту заказов" из формы авторизации')
    def test_check_go_to_order_feed_from_personal_account_unauthorized(self, driver):
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account = PersonalAccountPage(driver)
        order_feed = OrderFeedPage(driver)

        personal_account.go_to_personal_account()
        order_feed.go_to_order_feed()
        text = order_feed.is_order_feed_visible().text
        assert text == 'Лента заказов'

    @allure.title('переход на "Ленту заказов" из Личного кабинета')
    def test_check_go_to_order_feed_from_personal_account_authorized(self, driver):
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        personal_account = PersonalAccountPage(driver)
        order_feed = OrderFeedPage(driver)
        personal_account.authorization(UserData.email, UserData.password)
        personal_account.go_to_personal_account()
        order_feed.go_to_order_feed()
        text = order_feed.is_order_feed_visible().text
        assert text == 'Лента заказов'

    @allure.title('переход на "Ленту заказов" из Конструктора')
    def test_check_go_to_order_feed_from_constructor(self, driver):
        driver.get(Url.URL_HOME)
        order_feed = OrderFeedPage(driver)

        order_feed.go_to_order_feed()
        text = order_feed.is_order_feed_visible().text
        assert text == 'Лента заказов'

    @pytest.mark.parametrize("index", range(1, 3))
    @allure.title('открытие всплывающего окна с деталями ингредиента и закрытия этого окна')
    def test_check_ingredient_details_go_to_ingredient(self, driver, index):
        driver.get(Url.URL_HOME)
        constructor = ConstructorPage(driver)

        constructor.go_to_ingredient_by_index(index)
        constructor.close_ingredient_details()
        text = constructor.is_ingredient_details_visible().text
        assert text == 'Детали ингредиента'

    @pytest.mark.parametrize("index", range(1, 3))
    @allure.title('увеличение каунтера ингредиента при добавлении ингредиента в заказ')
    def test_drag_and_drop_ingredient_with_counter(self, driver, index):
        driver.get(Url.URL_HOME)
        constructor = ConstructorPage(driver)

        constructor.drag_and_drop_ingredient_by_counter(index)
        counter = constructor.get_counter_value(index)
        assert counter > 0
        
