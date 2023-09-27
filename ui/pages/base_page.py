from selenium.common import NoSuchElementException


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

# Функция открытия страницы
    def open(self):
        self.driver.get(self.url)

# Функция проверки существования объекта
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
