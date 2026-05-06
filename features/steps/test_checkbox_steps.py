from pytest_bdd import scenario, given, when, then, parsers
from utility.Log import get_logger

log = get_logger(__name__)

@scenario("../features/checkbox.feature", "Expand and select parent node")
def test_checkbox_tree(web_driver):
    pass

@given("the Elements > Checkbox page is open")
def open_checkbox_page(checkbox_page):
    checkbox_page.navigate_to_checkbox()

@when("the tree is expanded at all levels")
def expand_tree(checkbox_page):
    checkbox_page.expand_tree()

@when(parsers.parse('the parent node "{parent_name}" is ticked'))
def tick_parent(checkbox_page, parent_name):
    checkbox_page.tick_checkbox(name=parent_name)

@then(parsers.parse('all nested elements under "{parent_name}" have correct checked icons'))
def assert_child_icons(checkbox_page, parent_name):
    child_checkboxes = checkbox_page.get_check_leaf_result(parent_node=parent_name)
    assert all(child_checkboxes), f"Child checkbox under {parent_name} is not selected!"
    log.info(f'<PASSED>- All child nodes below parent node -> {parent_name} were selected successfully')
    log.info('======================================================================')
    log.info('Successfully completed the test')
    log.info('======================================================================')
