import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def test_redirect_is_correct(driver):
    driver.get('https://www.sberbank.ru/')
    driver.find_element(By.XPATH, "(//a[text()='Курсы валют'])[1]").click()
    page_title = driver.find_element(By.XPATH, "(//h1)[1]").text
    assert page_title == 'Курсы валют'
    driver.find_element(By.XPATH, "((//a[text()='Офисы'])[2]").click()
    page_title = driver.find_element(By.XPATH, "(//h1)[1]").text
    assert page_title == 'Офисы и банкоматы'
    driver.find_element(By.XPATH, "((//a[text()='Банкоматы'])[2]").click()
    page_title = driver.find_element(By.XPATH, "(//h1)[1]").text
    assert page_title == 'Офисы и банкоматы'
    driver.find_element(By.CSS_SELECTOR, "a.kitt-header__link.kitt-header__sbol").click()
    page_title = driver.find_element(By.CSS_SELECTOR, "button.Y3r81AWwgTQrGLMrRrkj").text
    assert page_title == 'Вход по номеру телефона'


def test_search(driver):
    driver.get('http://www.sberbank.ru/')
    driver.find_element(By.CSS_SELECTOR, "a.kitt-header-search").click()
    find_button = driver.find_element(By.CSS_SELECTOR, "input.kitt-header-search__search")
    find_button.click()
    find_button.send_keys('Кредит')
    driver.find_element(By.CSS_SELECTOR, "button.kitt-header-search__submit").click()
    time.sleep(1)
    word = driver.find_element(By.CSS_SELECTOR, "div.kit-checkbox__text").text
    assert word == "Поиск в документах"


def test_elements_counter(driver):
    driver.get('https://www.sberbank.ru/')
    rate_counter = len(driver.find_elements(By.XPATH, "(//a[text()='Курсы валют'])"))
    assert rate_counter == 4
    offices_counter = len(driver.find_elements(By.XPATH, "(//a[text()='Офисы'])"))
    assert offices_counter == 4
    atms_counter = len(driver.find_elements(By.XPATH, "(//a[text()='Банкоматы'])"))
    assert atms_counter == 4
    sbol_counter = len(driver.find_elements(By.XPATH, "(//a[text()='СберБанк Онлайн'])"))
    assert sbol_counter == 1


def test_color_link(driver):
    driver.get('http://www.sberbank.ru/')
    rate_counter = driver.find_element(By.XPATH, "(//a[text()='Курсы валют'])[1]")
    color_before = rate_counter.value_of_css_property("color")
    ActionChains(driver).move_to_element(rate_counter).perform()
    color_after = rate_counter.value_of_css_property("color")
    assert color_before != color_after
    offices_counter = driver.find_element(By.XPATH, "(//a[text()='Офисы'])[2]")
    color_before = offices_counter.value_of_css_property("color")
    ActionChains(driver).move_to_element(offices_counter).perform()
    color_after = offices_counter.value_of_css_property("color")
    assert color_before != color_after
    atms_counter = driver.find_element(By.XPATH, "(//a[text()='Банкоматы'])[2]")
    color_before = atms_counter.value_of_css_property("color")
    ActionChains(driver).move_to_element(atms_counter).perform()
    color_after = atms_counter.value_of_css_property("color")
    assert color_before != color_after
    sbol_counter = driver.find_element(By.XPATH, "(//a[text()='СберБанк Онлайн'])")
    color_before = sbol_counter.value_of_css_property("color")
    ActionChains(driver).move_to_element(sbol_counter).perform()
    color_after = sbol_counter.value_of_css_property("color")
    assert color_before != color_after


"""5 задание, по моему субъективному мнению не до конца понятно/подробно описано. Что конкретно требуется я не понял."""


def test_redirect(driver):
    try:
        driver.get('https://www.sberbank.ru/')
        driver.find_element(By.XPATH, "(//a[text()='СберБанк Онлайн'])").click()
        assert driver.find_element(By.CSS_SELECTOR, "h2.nt-widget__title").text == "Новости"
        driver.switch_to.window(driver.window_handles[0])
        driver.switch_to.window(driver.window_handles[0])
        driver.switch_to.window(driver.window_handles[0])
    finally:
        driver.quit()