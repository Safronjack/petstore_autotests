import pytest

from selenium import webdriver


# @pytest.fixture(scope='function', autouse=True)
# def driver(request):
#     # Параметры драйвера
#     options = webdriver.ChromeOptions()
#     options.add_argument('ignore-certificate-errors')
#     # Инициализация драйвера
#     driver = webdriver.Chrome(options=options)
#     # Настройки драйвера
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     request.addfinalizer(driver.quit)
#     return driver
#     # yield driver.quit()

#
# def pytest_addoption(parser):
#     parser.addoption("--driver",
#                      action="store",
#                      defoult="Chrome",
#                      help="Available browsers: Chrome, FireFox, Sber, Yandex",
#                      choices=["Chorme", "FireFox", "Sber", "Yandex"]
#                      )
#
#
# @pytest.fixture(scope='function', autouse=True)
# def driver(pytestconfig):
#     driver = pytestconfig.getoption("driver")
#     yield driver
