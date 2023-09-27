import time

import pytest
from selenium.webdriver.common.action_chains import ActionChains

from ui.steps import support_steps
from ui.pages.locators import *
from ui.pages.main_page import MainPage


@pytest.mark.parametrize('region',
                         [
                             'Московская',
                             'Ростов',
                             'Ростовская об',
                             'РоСт',
                             'карелия'
                         ],
                         ids=['Moscow', 'Rostov', 'Part of region', 'CamelCase', 'region']
                         )
def test_check_geoposition(driver, region):
    page = MainPage(driver, 'http://www.sberbank.ru/')
    # Открываем страницу
    page.open()
    # Нажимаем на смену региона
    page.geoposition_link()
    # Вводим название региона
    page.fill_text_region_name_field(region)
    # Нажимаем на найденный регион
    page.click_on_region_name(region)
    # Проверяем изменение региона
    page.assert_region_name_in_geo_link(region)


def test_exchange_rate_button(driver):
    page = MainPage(driver, 'http://www.sberbank.ru/')
    # Открываем страницу
    page.open()
    # Находим и проверяем наличие кнопки "Курсы валют"
    page.should_be_exchange_rate_link()
    # Кликаем по кнопке
    page.click_on_exchange_rate_link()
    # Проверяем, что мы на нужной странице
    page.assert_exchange_rate_title()


# Проверка функциональных кнопок хедера главной строницы
def test_sber_main(driver):
    try:
        # Переходим на главную страницу
        driver.get('http://www.sberbank.ru/')
        # Меняем язык
        driver.find_element.HEADER_LANGUAGE_CHANGE.click()
        time.sleep(1)
        # Возвращаем русский язык
        driver.find_element.HEADER_ENG_LANGUAGE_CHANGE.click()
        time.sleep(1)
        # Нажимаем на кнопку поиска
        driver.find_element.HEADER_SEARCH_BUTTON.click()
        # Ставим каретку в инзут поиска
        find_button = driver.find_element.HEADER_SEARCH_INPUTLINE
        find_button.click()
        # Вводим тестовый запрос
        find_button.send_keys(support_steps.generate_random_string(7))
        # Нажимаем на кнопку поиска
        driver.find_element.HEADER_SEARCH_FIND_BUTTON.click()
        time.sleep(1)
        driver.find_element.HEADER_SEARCH_BUTTON.click()
        find_button = driver.find_element.HEADER_SEARCH_INPUTLINE
        find_button.click()
        find_button.send_keys('')
        driver.find_elementHEADER_SEARCH_FIND_BUTTON.click()
        time.sleep(2)
    finally:
        driver.quit()


# Проверка изменения цвета кнопок при наведении курсора
def test_text_color_header_button(driver):
    try:
        # Переходим на главную страницу
        driver.get('http://www.sberbank.ru/')
        # Курсы валют
        button = driver.find_elementHEADER_EXCHANGE_RATE_BUTTON
        ActionChains(driver).move_to_element(button).perform()
        time.sleep(2)
        # Офисы
        button = driver.find_element.HEADER_OFFICES_BUTTON
        ActionChains(driver).move_to_element(button).perform()
        time.sleep(2)
        # Банкоматы
        button = driver.find_element.HEADER_ATMS_BUTTON
        ActionChains(driver).move_to_element(button).perform()
        time.sleep(2)
        # Смена региона
        button = driver.find_element.HEADER_REGION_CHANGE_BUTTON
        ActionChains(driver).move_to_element(button).perform()
        time.sleep(2)
        # Кнопка поиска
        button = driver.find_element.HEADER_SEARCH_BUTTON
        ActionChains(driver).move_to_element(button).perform()
        time.sleep(2)
    finally:
        driver.quit()


def test_sber_main_negative(driver):
    try:
        driver.get('http://www.sberbank.ru/')
        driver.find_element(By.XPATH, "(//test").click()
        time.sleep(1)
    finally:
        driver.quit()
