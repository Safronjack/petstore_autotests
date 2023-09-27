main_url = 'https://petstore.swagger.io/v2/'

pet_url = 'https://petstore.swagger.io/v2/pet/'
user_url = 'https://petstore.swagger.io/v2/user/'
cart_url = 'https://petstore.swagger.io/v2/cart/'


def pet_url_plus_query(query):
    return pet_url + str(query)


def user_url_plus_query(query):
    return user_url + str(query)


def cart_url_plus_query(query):
    return cart_url + str(query)

