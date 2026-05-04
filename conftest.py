import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from POM.Books import Books
from POM.Checkbox import Checkbox
from POM.DynamicProperties import DynamicProperties
from POM.Form import Form
from utility.Log import get_logger
import datetime

log = get_logger(__name__)

@pytest.fixture(scope='function', params=['chrome'])
def web_driver(request):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")

    log.info('======================================================================')
    log.info(f'Initializing {request.param} browser')
    log.info('======================================================================')

    log.info('======================================================================')
    log.info(f'Starting test :: {request.node.name} to verify checkbox')
    log.info('======================================================================')

    if request.param == 'chrome':
        driver = webdriver.Chrome(options=options)
    if request.param == 'edge':
        driver = webdriver.Edge(options=options)

    yield driver

    log.info('======================================================================')
    log.info(f'Closing {request.param} browser')
    log.info('======================================================================')
    driver.close()
    driver.quit()

@pytest.fixture
def checkbox_page(web_driver):
    return Checkbox(web_driver)

@pytest.fixture
def dynamic_properties_page(web_driver):
    return DynamicProperties(web_driver)

@pytest.fixture
def practice_form(web_driver, request):
    return Form(web_driver)

@pytest.fixture
def books(web_driver, request):
    return Books(web_driver)

def pytest_configure(config):
    # Format: YYYY-MM-DD_HH-MM-SS
    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    # Safely set HTML report path
    if not getattr(config.option, "htmlpath", None):
        config.option.htmlpath = f"reports/html_reports/html-report-{timestamp}.html"