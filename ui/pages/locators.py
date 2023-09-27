from selenium.webdriver.common.by import By


class BasePageLocators:
    FIRST_PAGE_TITLE = (By.XPATH, "(//h1)[1]")


class MainPageLocators(BasePageLocators):
    HEADER_LANGUAGE_CHANGE = (By.XPATH, "//a[text()='ENG'])[1]")
    HEADER_ENG_LANGUAGE_CHANGE = (By.CSS_SELECTOR, "a.kitt-header__lang_ru")
    HEADER_SEARCH_BUTTON = (By.CSS_SELECTOR, "a.kitt-header-search")
    HEADER_SEARCH_INPUTLINE = (By.CSS_SELECTOR, "input.kitt-header-search__search")
    HEADER_SEARCH_FIND_BUTTON = (By.CSS_SELECTOR, "button.kitt-header-search__submit")
    HEADER_EXCHANGE_RATE_BUTTON = (By.XPATH, "(//a[text()='Курсы валют'])[1]")
    HEADER_OFFICES_BUTTON = (By.XPATH, "(//a[text()='Офисы'])[2]")
    HEADER_ATMS_BUTTON = (By.XPATH, "(//a[text()='Банкоматы'])[2]")
    HEADER_REGION_CHANGE_BUTTON = (By.CSS_SELECTOR, ".kitt-header__link.kitt-header__region.kitt-header-region-show")
    CHANGE_REGION_INPUT_FIELD = (By.CSS_SELECTOR, ".kitt-header-region__search")
    CHANGE_REGION_REGION_NAME = (By.CSS_SELECTOR, "li.kitt-header-region__item:first-child "
                                                  "button.kitt-header-region__region")
