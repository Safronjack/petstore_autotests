import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


"""Определение драйвера вынесено в conftest как фикстура По какой то причине на странице сбера page_down крутит в 
футер страницы, хотя на других сайтах все отлично отрабатывает. Могу предположить, что это баг СберКрафта 
(конструктор фронтов новый, вышел этим летом и еще имеет кучу багов) 

Так же в следующем разделе отсутствует нипут для ввода ссылки на репозиторий, так что реализую задание в этом файле"""


def test_scroll(driver):
    try:
        driver.get('https://www.sberbank.ru/')
        time.sleep(1)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)
        time.sleep(2)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
        time.sleep(2)
    finally:
        driver.quit()


def test_switch(driver):
    try:
        driver.get('https://www.sberbank.ru/')
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "span.kitt-top-menu__link-text.kitt-top-menu__link-text_external").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
    finally:
        driver.quit()


def test_counter(driver):
    try:
        driver.get('https://www.sberbank.ru/')
        offices_counter = driver.find_elements(By.XPATH, "(//a[text()='Офисы'])")
        print("offices count = ", len(offices_counter))
        atms_counter = driver.find_elements(By.XPATH, "(//a[text()='Банкоматы'])")
        print("atms count = ", len(atms_counter))
    finally:
        driver.quit()
