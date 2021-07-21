import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Chrome Browser..............")
    elif browser == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
    elif browser == 'safari':
        driver = webdriver.Safari()
        print("Launching Safari Browser..............")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Daniel Montoya'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
