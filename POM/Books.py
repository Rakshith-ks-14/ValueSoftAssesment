from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from POM.Base import Base
from utility.CustomExceptions import PageNotLoadedException, InvalidResponseException
import requests


class Books(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.books_xpath = (By.XPATH, '//a[@href="/books"]')
        self.books = (By.XPATH, '//div[@class="books-wrapper"]')
        self.column_name = './/table//th'
        self.rows = './/table/tbody/tr'
        self.next = (By.XPATH, '//button[text()="Next"]')

    def navigate_to_books(self):
        self.open_url()
        self.click_on_element(locator=self.books_xpath)
        try:
            self.wait_till_visible(locator=self.books, timeout=10, name='Book Page')
        except TimeoutException:
            raise PageNotLoadedException(msg='Books page not loaded successfully..!')

        self.log.info('Successfully navigated to "Books" page')

    def get_all_books(self):
        books = self.driver.find_element(*self.books)
        all_books = []
        columns = [col.text.lower() for col in books.find_elements(By.XPATH, self.column_name)[1:]]
        while True:
            for row in books.find_elements(By.XPATH, self.rows):
                book = {c: v.text for c, v in zip(columns, row.find_elements(By.XPATH, './td')[1:])}
                all_books.append(book)
            try:
                self.click_on_element(locator=self.next)
            except TimeoutException:
                break
        return all_books

    def get_all_books_api(self):
        base_url = self.read_json.get_data(key_name='url')
        books_url = self.read_json.get_data(key_name='get_all_book_api')
        response = requests.get(url=base_url+books_url, verify=False)
        if response.status_code == 200:
            all_books = [{'title': res['title'], 'author': res['author'], 'publisher': res['publisher']}
                         for res in response.json()['books']]
        else:
            raise InvalidResponseException(f'Expected status code 200 not matching with actual {response.status_code}')
        return all_books

    def compare_gui_api_data(self, gui_data, api_data):
        for key, value in gui_data:
            if gui_data[key] == api_data[key]:
                self.log.info(f'<PASSED>- The {key} of GUI data -> {gui_data[key]} is matching with API data -> {api_data[key]}')