import allure
import pytest

from rest.resources import urls as urls
from rest.steps import support_steps as support_steps
from rest.steps import generate_json_steps as generate_json_steps
from rest.steps import request_steps as request_steps
from rest.steps import assert_steps as assert_steps

# Переменная для хранения id созданного питомца
ids = None


# Сценарий удаления записи питомца
@allure.step
@pytest.mark.smoke
@pytest.mark.regress
def test_delete_pet():
    with allure.step("Проверка сценария удаления записи питомца"):
        request = request_steps.request_post(urls.pet_url, generate_json_steps.generate_json_post_pet_with_all_params())
        ids = str(request.json()['id'])
        request_steps.request_delete(urls.pet_url + ids)
    with allure.step("Проверка ответа от API"):
        assert assert_steps.assert_status_code_equal_200
