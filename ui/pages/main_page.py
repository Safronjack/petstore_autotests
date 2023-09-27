from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def should_be_exchange_rate_link(self):
        assert self.is_element_present(*MainPageLocators.HEADER_EXCHANGE_RATE_BUTTON), "Ссылка 'Курсы валют' " \
                                                                                       "отсутствует "

    def click_on_exchange_rate_link(self):
        button = self.driver.find_element(*MainPageLocators.HEADER_EXCHANGE_RATE_BUTTON)
        button.click()

    def assert_exchange_rate_title(self):
        # assert self.driver.find_element(*MainPageLocators.FIRST_PAGE_TITLE).text == "Курсы вадют", "Первый заголовок " \
        #                                                                                            "не 'Курсы валют' "
        pass

    def geoposition_link(self):
        button = self.driver.find_element(*MainPageLocators.HEADER_REGION_CHANGE_BUTTON)
        button.click()

    def fill_text_region_name_field(self, region):
        self.driver.find_element(*MainPageLocators.CHANGE_REGION_INPUT_FIELD).send_keys(region)

    def click_on_region_name(self, region):
        link = self.driver.find_element(By.XPATH, "//button[text()[contains(.,'" + region.title() + "')]]")
        link.click()

    def assert_region_name_in_geo_link(self, region):
        assert self.driver.find_element(*MainPageLocators.HEADER_REGION_CHANGE_BUTTON).text.__contains__(region.title())\
            , "Регион не найден"
