from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from POM.Base import Base
from utility.CustomExceptions import PageNotLoadedException


class DynamicProperties(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.elements_xpath = (By.XPATH, '//a[@href="/elements"]')
        self.elements_page_title = (By.XPATH, '//div[text()="Please select an item from left to start practice."]')
        self.dynamic_xpath = (By.XPATH, '//span[text()="Dynamic Properties"]')
        self.dynamic_title = (By.XPATH, '//h1[text()="Dynamic Properties"]')
        self.dynamic_button_ele = (By.XPATH, '//button[@id="visibleAfter"]')
        self.dynamic_button_color = (By.XPATH, '//button[text()="Color Change"]')

    def navigate_to_dynamic_properties(self):
        self.open_url()
        self.click_on_element(locator=self.elements_xpath)
        try:
            self.wait_till_visible(locator=self.elements_page_title, timeout=10, name='Elements Page')
        except TimeoutException:
            raise PageNotLoadedException(msg='Elements page not loaded successfully..!')

        self.log.info('Successfully navigated to "Elements" page')

        self.click_on_element(locator=self.dynamic_xpath)

        try:
            self.wait_till_visible(locator=self.dynamic_title, timeout=10, name='Dynamic Properties Page')
        except TimeoutException:
            raise PageNotLoadedException(msg='Dynamic Properties page not loaded successfully..!')
        self.log.info('Successfully navigated to "Dynamic Properties" page')

    def check_for_button_presence(self, timeout):
        try:
            self.wait_till_visible(locator=self.dynamic_button_ele, timeout=timeout, name='Dynamic Button')
            return True
        except TimeoutException:
            return False

    def get_button_color(self, locator):
        dynamic_color_button = self.driver.find_element(*locator)
        rgba_color = dynamic_color_button.value_of_css_property("color")
        return self.find_color(rgba_color=rgba_color)
