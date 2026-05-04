from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from POM.Base import Base
from utility.CustomExceptions import PageNotLoadedException


class Form(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.form_xpath = (By.XPATH, '//a[@href="/forms"]')
        self.form_page_title = (By.XPATH, '//div[text()="Please select an item from left to start practice."]')
        self.practice_form_xpath = (By.XPATH, '//span[text()="Practice Form"]')
        self.practice_form_title = (By.XPATH, '//h1[text()="Practice Form"]')
        self.first_name = (By.ID, 'firstName')
        self.last_name = (By.ID, 'lastName')
        self.email = (By.ID, 'userEmail')
        self.mobile_no = (By.ID, 'userNumber')
        self.dob = (By.ID, 'dateOfBirthInput')
        self.subjects = (By.ID, 'subjectsInput')
        self.picture = (By.ID, 'uploadPicture')
        self.current_address = (By.ID, 'currentAddress')
        self.hobbies = (By.XPATH, '//div[@id="hobbiesWrapper"]//div[contains(@class, "form-check")]/label')
        self.year = (By.XPATH, '//select[@class="react-datepicker__year-select"]')
        self.month = (By.XPATH, '//select[@class="react-datepicker__month-select"]')
        self.submit = (By.ID, 'submit')
        self.success_pop_up = (By.XPATH, '//div[@class="modal-content"]')
        self.success_msg = (By.XPATH, '//div[@class="modal-header"]')

    def navigate_to_practice_form(self):
        self.open_url()
        self.click_on_element(locator=self.form_xpath)
        try:
            self.wait_till_visible(locator=self.form_page_title, timeout=10, name='Form Page')
        except TimeoutException:
            raise PageNotLoadedException(msg='Form page not loaded successfully..!')

        self.log.info('Successfully navigated to "Form" page')

        self.click_on_element(locator=self.practice_form_xpath)

        try:
            self.wait_till_visible(locator=self.practice_form_title, timeout=10, name='Practice Form')
        except TimeoutException:
            raise PageNotLoadedException(msg='Practice Form page not loaded successfully..!')
        self.log.info('Successfully navigated to "Practice Form" page')

    def fill_name(self, first_name, last_name):
        self.log.info(f'Filling First Name -> {first_name} and Last Name -> {last_name}')
        self.fill_data(locator=self.first_name, data=first_name)
        self.fill_data(locator=self.last_name, data=last_name)

    def fill_email(self, email_id):
        self.log.info(f'Filling Email ID -> {email_id}')
        self.fill_data(locator=self.email, data=email_id)

    def fill_gender(self, gender):
        self.log.info(f'Filling Gender -> {gender}')
        locator = (By.XPATH, f'//input[@value="{gender.capitalize()}"]')
        self.click_on_element(locator=locator)

    def fill_mobile_no(self, mobile_no):
        self.log.info(f'Filling Mobile No. -> {mobile_no}')
        self.fill_data(locator=self.mobile_no, data=mobile_no)

    def fill_subject(self, subject):
        self.log.info(f'Filling Subject -> {subject}')
        self.fill_data(locator=self.subjects, data=subject)

    def fill_hobbies(self, hobbies):
        self.log.info(f'Filling Hobbies -> {hobbies}')
        hobbies_name = [ele.text for ele in self.driver.find_elements(*self.hobbies)]
        if all(map(lambda hobby: hobby in hobbies_name, hobbies)):
            for hob in hobbies:
                locator = (By.XPATH, f'//div[@id="hobbiesWrapper"]//div[contains(@class, "form-check")]'
                                     f'/label[text()="{hob}"]/ancestor::div/input')
                self.click_on_element(locator=locator)

    def upload_file(self, file_name_path):
        self.log.info(f'Uploading File -> {file_name_path}')
        self.fill_data(locator=self.picture, data=file_name_path)

    def fill_current_address(self, address):
        self.log.info(f'Filling Address -> {address}')
        self.fill_data(locator=self.current_address, data=address)

    def date_picker(self, year, month, date):
        self.log.info(f'Filling Year -> {year}, Month -> {month} and Date -> {date}')
        self.click_on_element(locator=self.dob)
        self.wait_till_visible(locator=self.year, timeout=10, name='Select Option')
        self.select_option(locator=self.year, option=year)
        self.select_option(locator=self.month, option=month)
        date_ele = (By.XPATH, f'//div[contains(@aria-label, "{month}")][text()="{date}"]')
        self.click_on_element(locator=date_ele)

    def click_submit(self):
        self.log.info(f'Clicking submit button')
        self.click_on_element(locator=self.submit)

    def get_form_submission_result(self, success_msg):
        try:
            self.wait_till_visible(locator=self.success_pop_up, timeout=10, name='Success Popup')
            msg = self.get_text(locator=self.success_msg)
            if msg == success_msg:
                return True
            else:
                return False
        except TimeoutException:
            return False

    def get_border_color(self, locator):
        field_ele = self.driver.find_element(*locator)
        self.click_on_element(locator=locator)
        rgba_color = field_ele.value_of_css_property("border-color")
        return self.find_color(rgba_color=rgba_color)
