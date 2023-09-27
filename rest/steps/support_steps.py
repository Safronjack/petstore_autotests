import random
import string


def generate_random_int(len):
    result = ""
    for i in range(0, len):
        result += str(random.randint(0, 9))
    return result


def generate_random_phone_number():
    prefix = str(8)
    result = ""
    for i in range(0, 10):
        result += str(random.randint(0, 9))
    return prefix + result


def generate_random_string(len):
    result = ""
    for i in range(0, len):
        result += str(random.choice(string.ascii_letters[random.randint(0, 5)]))
    return result


def generate_random_email(len):
    host = "@test.com"
    result = ""
    for i in range(0, len):
        result += str(random.choice(string.ascii_letters[random.randint(0, 5)]))
    return result + host


def generate_random_link(len):
    prefix = "https://www."
    sufix = ".com"
    result = ""
    for i in range(0, len):
        result += str(random.choice(string.ascii_letters[random.randint(0, 5)]))
    return prefix + result + sufix
