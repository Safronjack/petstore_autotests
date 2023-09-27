# import allure
# import pytest
#
# from rest.resources import urls as urls
# from rest.steps import support_steps as support_steps
# from rest.steps import generate_json_steps as generate_json_steps
# from rest.steps import request_steps as request_steps
# from rest.steps import assert_steps as assert_steps
#
# # Переменная для хранения id созданного питомца
# ids = None
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
# def test_post_pet_negative(scenario):
#     with allure.step("Негативный сценарий отправки запроса на создание питомца"):
#         request = request_steps.request_post(urls.pet_url, scenario)
#     with allure.step("Проверка ответа от API"):
#         assert request.json()["message"] == "something bad happened"
#
#
# # # Создание записи питомца
# @allure.step
# @pytest.mark.smoke
# @pytest.mark.regress
# def test_post_pet():
#     with allure.step("Сценарий отправки запроса на создание нового питомца"):
#         global ids
#         request = request_steps.request_post(urls.pet_url, generate_json_steps.generate_json_post_pet_with_all_params())
#         response = request.json()
#         ids = response['id']
#     with allure.step("Проверка ответа от API"):
#         assert_steps.assert_status_code_equal_200(request)
#
#
# # Получение записи питомца
# @allure.step
# @pytest.mark.smoke
# @pytest.mark.regress
# def test_get_pet():
#     with allure.step("Сценарий проверки метода получения записи питомца"):
#         request = request_steps.request_get(urls.pet_url_plus_query(ids))
#     with allure.step("Проверка ответа от API"):
#         assert_steps.assert_json_is_not_none(request)
#
#
# # Негативный сценарий получения записи питомца
# @allure.step
# @pytest.mark.parametrize(
#     "scenario",
#     [
#         {"id": support_steps.generate_random_string(5)},
#         {"id": support_steps.generate_random_email(5)}
#     ],
#     ids=["string", "some_query"]
# )
# @allure.step
# @pytest.mark.smoke
# @pytest.mark.regress
# @pytest.mark.negative
# def test_get_pet(scenario):
#     with allure.step("Сценарий проверки метода получения записи питомца"):
#         request = request_steps.request_get(urls.pet_url_plus_query(scenario))
#     with allure.step("Проверка ответа от API"):
#         assert_steps.assert_json_is_not_none(request)
#
#
# # Негативный сценарий изменения карточки питомца
# @allure.step
# @pytest.mark.parametrize(
#     'scenario',
#     [
#         {'name': support_steps.generate_random_int(5)},
#         {'name': support_steps.generate_random_phone_number()}
#     ],
#     ids=["int", "phone"]
# )
# @pytest.mark.regress
# @pytest.mark.negative
# def test_post_pet_negative(scenario):
#     with allure.step("Негативный сценарий изменения карточки питомца"):
#         request_steps.request_post(urls.pet_url, generate_json_steps.generate_json_post_pet_with_all_params())
#         body = {
#             'id': ids,
#             'name': scenario,
#             'category': {
#                 'name': support_steps.generate_random_string(3)
#             },
#             'photoUrls': [support_steps.generate_random_string(5)]
#         }
#         request = request_steps.request_put(urls.pet_url, body)
#     with allure.step("Проверка ответа от API"):
#         assert request.json()["message"] == "something bad happened"
#         assert assert_steps.assert_status_code_equal_500
#
#
# # Сценарий изменения карточки питомца
# @allure.step
# @pytest.mark.regress
# def test_put_pet():
#     with allure.step("Проверка метода изменения карточки питомца"):
#         body = {
#             'id': ids,
#             'name': support_steps.generate_random_string(5),
#             'category': {
#                 'name': support_steps.generate_random_string(3)
#                         },
#             'photoUrls': [support_steps.generate_random_string(5)]
#         }
#         request_steps.request_put(urls.pet_url, body)
#     with allure.step("Проверка ответа от API"):
#         assert assert_steps.assert_status_code_equal_200
#
#
# # Сценарий удаления записи питомца
# @allure.step
# @pytest.mark.smoke
# @pytest.mark.regress
# def test_delete_pet():
#     with allure.step("Проверка сценария удаления записи питомца"):
#         request = request_steps.request_post(urls.pet_url, generate_json_steps.generate_json_post_pet_with_all_params())
#         ids = str(request.json()['id'])
#         request_steps.request_delete(urls.pet_url + ids)
#     with allure.step("Проверка ответа от API"):
#         assert assert_steps.assert_status_code_equal_200
