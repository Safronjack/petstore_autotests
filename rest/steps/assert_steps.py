import allure


# Проверка статус кода == 200
def assert_status_code_equal_200(request):
    with allure.step('Проверка статус кода == 200'):
        assert request.status_code == 200


# Проверка статус кода == 405
def assert_status_code_equal_405(request):
    with allure.step('Проверка статус кода == 405'):
        assert request.status_code == 405


# Проверка статус кода == 500
def assert_status_code_equal_500(request):
    with allure.step('Проверка статус кода == 500'):
        assert request.status_code == 500


# Проверка ответа метода о ненайденном пользователе
def assert_user_not_found(request):
    with allure.step('Проверка сообщения бэка: User not found'):
        assert request.json()["message"] == "User not found"


# Проверка json тела ответа
def assert_json_is_not_none(request):
    assert request.json() is not None
