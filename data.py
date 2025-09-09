DRIVER_NAME = None


# URL
class Url:
    BASE_URL = "https://stellarburgers.nomoreparties.site"

    URL_HOME = f"{BASE_URL}/"  # Домашняя страница (Конструктор)
    URL_ENTRANCE_PERSONAL_ACCOUNT = f"{BASE_URL}/login"  # Форма авторизации
    URL_ACCOUNT_PROFILE = f"{BASE_URL}/account/profile"  # Личный кабинет (Профиль)
    URL_ORDER_HISTORY = f"{BASE_URL}/account/order-history"  # История заказов
    URL_ORDER_FEED = f"{BASE_URL}/feed"  # Лента заказов


# Данные для авторизации
class UserData:
    email = 'lexa.d.nik@yandex.ru'
    password = '123456'
