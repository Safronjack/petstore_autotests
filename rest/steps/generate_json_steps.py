import allure

from rest.steps import support_steps as support_steps


# Генерация JSON для POST метода User со всеми параметрами
def generate_json_post_user_with_all_params():
    with allure.step('Генерация JSON для POST метода /user'):
        body = {
            "username": support_steps.generate_random_string(5),
            "firstName": support_steps.generate_random_string(5),
            "lastName": support_steps.generate_random_string(5),
            "email": support_steps.generate_random_email(5),
            "password": support_steps.generate_random_string(5),
            "phone": support_steps.generate_random_phone_number(),
            "userStatus": support_steps.generate_random_int(2)
        }
        return body


# Генерация JSON для POST метода Pet со всеми параметрами
def generate_json_post_pet_with_all_params():
    with allure.step('Генерация JSON для POST метода /pet'):
        body = {
            'name': support_steps.generate_random_string(5),
            'category': {
                'name': support_steps.generate_random_string(3)
                        },
            'photoUrls': [support_steps.generate_random_string(5)]
        }
        return body
