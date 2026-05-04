import pytest
from pytest_bdd import scenario, given, when, then
from conftest import books
from utility.Log import get_logger

log = get_logger(__name__)

@scenario("../features/books.feature", "Validate book list against API")
def test_success_form_submission(web_driver):
    pass

@pytest.fixture
def context():
    return {}

@given("the user navigates to the Book Store page")
def navigate_to_bookstore(books):
    books.navigate_to_books()

@when("the list of books is displayed on the page")
def get_ui_books(books, context):
    gui_book_data = books.get_all_books()
    context['gui_book_data'] = gui_book_data

@when("the user retrieves the list of books from the API")
def retrieve_api_books(books, context):
    api_books_data = books.get_all_books_api()
    context['api_books_data'] = api_books_data

@then("the number of books displayed should equal the number of books in the API")
def compare_book_count(context):
    assert len(context['gui_book_data']) == len(context['api_books_data']), '<ERROR>-Length mismatching'
    log.info('<PASSED>- Length matched successfully')

@then("the book titles, authors and publishers on the page should match the API response")
def compare_books(context):
    gui_data = context['gui_book_data']
    api_data = context['api_books_data']
    for gui, api in zip(gui_data, api_data):
        assert gui == api, f'<ERROR>- The GUI data -> {gui} is not matching with API data -> {api}'
        log.info(f'<PASSED>- The GUI data -> {gui} is matching with API data -> {api}')
    log.info('======================================================================')
    log.info('Successfully completed the test')
    log.info('======================================================================')

