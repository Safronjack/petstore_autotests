# import allure
# import pytest
#
# from rest.resources import urls as urls
# from rest.steps import support_steps as support_steps
# from rest.steps import generate_json_steps as generate_json_steps
# from rest.steps import request_steps as request_steps
# from rest.steps import assert_steps as assert_steps
#
# # Переменная для хранения имени созданного пользователя
# some_name = ""
#
#
# # Негативный сценарий создания пользователя
# @allure.step
# @pytest.mark.parametrize(
#     "scenario",
#     [
#         {"id": support_steps.generate_random_string(5)},
#         {"id": support_steps.generate_random_email(5)}
#     ],
#     ids=["string", "some_query"]
# )
# @pytest.mark.regress
# @pytest.mark.negative
# def test_post_user_negative(scenario):
#     with allure.step("Негативный сценарий отправки запроса на создание пользователя"):
#         url = urls.user_url
#         body = scenario
#         request = request_steps.request_post(url, body)
#     with allure.step("Проверка ответа от API"):
#         assert request.json()["message"] == "something bad happened"
#
#
# # # Создание пользователя
# @allure.step
# @pytest.mark.smoke
# @pytest.mark.regress
# def test_post_user():
#     with allure.step("Сценарий отправки запроса на создание пользователя"):
#         global some_name
#         url = urls.user_url
#         body = generate_json_steps.generate_json_post_user_with_all_params()
#         some_name = body["username"]
#         request = request_steps.request_post(url, body)
#     with allure.step("Проверка ответа от API"):
#         assert_steps.assert_status_code_equal_200(request)
#
#
# # Получение записи пользователя
# @allure.step
# @pytest.mark.smoke
# @pytest.mark.regress
# def test_get_user():
#     with allure.step("Проверка метода получения записи пользователя"):
#         global some_name
#         request = request_steps.request_get(urls.user_url_plus_query(some_name))
#     # assert request.json()["username"] == some_name
#
#
# # Негативный сценарий получение записи пользователя
# @allure.step
# @pytest.mark.regress
# @pytest.mark.negative
# def test_get_user_negative():
#     with allure.step("Негативный сценарий проверки метода получения записи пользователя"):
#         request = request_steps.request_get(urls.user_url_plus_query(support_steps.generate_random_int(3)))
#     with allure.step("Проверка ответа от API"):
#         assert_steps.assert_user_not_found(request)
#
#
# # Негативный сценарий изменения карточки пользователя
# @allure.step
# @pytest.mark.regress
# @pytest.mark.negative
# def test_put_user_negative():
#     with allure.step("Негативный сценарий проверки метода изменения карточки пользователя"):
#         url = urls.user_url
#         body = generate_json_steps.generate_json_post_user_with_all_params()
#         request = request_steps.request_put(url, body)
#     with allure.step("Проверка ответа от API"):
#         assert_steps.assert_status_code_equal_405(request)
#
#
# # Сценарий изменения карточки пользователя
# @allure.step
# @pytest.mark.regress
# def test_put_user():
#     with allure.step("Проверка метода изменения карточки пользователя"):
#         global some_name
#         body = generate_json_steps.generate_json_post_user_with_all_params()
#         some_name = body["username"]
#         request = request_steps.request_put(urls.user_url_plus_query("Karasik"), body)
#     with allure.step("Проверка ответа от API"):
#         assert_steps.assert_status_code_equal_200(request)
#
#
# # Негативный сценарий удаления записи пользователя
# @allure.step
# @pytest.mark.regress
# @pytest.mark.negative
# def test_delete_user_negative():
#     with allure.step("Негативный сценарий метода удаления записи пользователя"):
#         request = request_steps.request_delete(urls.user_url)
#     with allure.step("Проверка ответа от API"):
#         assert_steps.assert_status_code_equal_405(request)
#
#
# # Сценарий удаления записи пользователя
# @allure.step
# @pytest.mark.smoke
# @pytest.mark.regress
# def test_delete_user():
#     with allure.step("Проверка сценария удаления записи пользователя"):
#         request = request_steps.request_delete(urls.user_url_plus_query(some_name))
#     # assert_steps.assert_status_code_equal_200(request)
