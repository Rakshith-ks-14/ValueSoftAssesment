import pytest
from pytest_bdd import scenario, given, when, then, parsers

from conftest import dynamic_properties_page
from utility.Log import get_logger

log = get_logger(__name__)

@scenario("../features/dynamic_properties.feature", "Verify dynamic button visibility and color change")
def test_dynamic_properties(web_driver):
    pass

@given('navigate to Elements > Dynamic Properties')
def navigate_dynamic_properties(dynamic_properties_page):
    dynamic_properties_page.navigate_to_dynamic_properties()

@pytest.fixture
def context():
    return {}

@when(parsers.parse('fluently wait for the button with text Visible after "{timeout}" seconds to be displayed'))
def wait_for_button(dynamic_properties_page, context, timeout):
    result = dynamic_properties_page.check_for_button_presence(timeout=timeout)
    context['result'] = result

@then('the button should be visible on the page')
def verify_button_visible(context):
    assert context['result'], f"<FAILED>- Dynamic button not loaded after some time"
    log.info('<PASSED>- Dynamic button loaded successfully after some time')

@when('refresh the page')
def refresh_page(dynamic_properties_page):
    dynamic_properties_page.page_reload()

@then(parsers.parse('the second button should change its color after some time "{timeout}"'))
def verify_color_change(dynamic_properties_page, timeout):
    previous_color = dynamic_properties_page.get_button_color(locator=dynamic_properties_page.dynamic_button_color)
    assert dynamic_properties_page.check_for_button_presence(timeout=timeout)
    present_color = dynamic_properties_page.get_button_color(locator=dynamic_properties_page.dynamic_button_color)
    assert previous_color != present_color, f"Expected color change, but remained {previous_color}"
    log.info(f'<PASSED>- Dynamic button successfully color change from -> {previous_color} to -> {present_color}')
    log.info('======================================================================')
    log.info('Successfully completed the test')
    log.info('======================================================================')