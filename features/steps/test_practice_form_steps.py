from platform import python_revision

import pytest
from pytest_bdd import scenario, given, when, then, parsers
from utility.Log import get_logger
from utility.ReadJson import ReadJson

log = get_logger(__name__)

@scenario("../features/forms.feature", "Successful form submission")
def test_success_form_submission(web_driver):
    pass

@scenario("../features/forms.feature", "unsuccessful form submission")
def test_invalid_form_submission(web_driver):
    pass

@scenario("../features/forms.feature", "form field validation")
def test_form_field_validation(web_driver):
    pass

@pytest.fixture
def context():
    return {}

@given("the user navigates to Forms > Practice Forms")
def navigate_to_form(practice_form):
    practice_form.navigate_to_practice_form()

@when("the user fills all required fields with valid data")
def fill_valid_data(practice_form, context):
    read_json = ReadJson()
    info = read_json.get_data(key_name='student_info')
    fill_form(form=practice_form, info=info)

@when("the user clicks the Submit button")
def click_submit(practice_form):
    practice_form.click_submit()

@then(parsers.parse('display a confirmation message "{success_msg}"'))
def confirmation_message(practice_form, success_msg):
    result = practice_form.get_form_submission_result(success_msg=success_msg)
    assert result

@when(parsers.parse('the user enters empty/invalid data "{invalid_data}" in the "{field_name}" field'))
def fill_invalid_data(practice_form, context, invalid_data, field_name):
    if invalid_data == 'None':
        invalid_data = ''
    context['field_name'] = field_name
    context['previous_color'] = practice_form.get_border_color(locator=getattr(practice_form, field_name))
    read_json = ReadJson()
    info = read_json.get_data(key_name='student_info')
    required_data = info
    required_data[field_name] = invalid_data
    fill_form(form=practice_form, info=required_data)

def fill_form(form, info):
    form.fill_name(first_name=info['first_name'], last_name=info['last_name'])
    form.fill_email(email_id=info['email'])
    form.fill_gender(gender=info['gender'])
    form.fill_mobile_no(mobile_no=info['mobile_no'])
    form.date_picker(year=info['year'], month=info['month'], date=info['date'])

@then(parsers.parse('it should not display a confirmation message "{success_msg}"'))
def message_not_display(practice_form, success_msg):
    result = practice_form.get_form_submission_result(success_msg=success_msg)
    assert result == False
    log.info('<PASSED>- Success popup did not appeared')

@then('the filed should change its color')
def filed_change_color(practice_form, context):
    present_color = practice_form.get_border_color(locator=getattr(practice_form, context['field_name']))
    assert present_color != context['previous_color']
    log.info(f'<PASSED>- Field name -> {context["field_name"]} showing error, changed color from -> '
             f'{context["previous_color"]} to -> {present_color}')
    log.info('======================================================================')
    log.info('Successfully completed the test')
    log.info('======================================================================')