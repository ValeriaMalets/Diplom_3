import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="session")
def chrome_driver_path():
    path = ChromeDriverManager().install()
    return path


@pytest.fixture(scope="session")
def firefox_driver_path():
    path = GeckoDriverManager().install()
    return path


@pytest.fixture(scope="function")
def browser(request, chrome_driver_path, firefox_driver_path):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        service = ChromeService(executable_path=chrome_driver_path)
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        service = FirefoxService(executable_path=firefox_driver_path)
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver

    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox"
    )
