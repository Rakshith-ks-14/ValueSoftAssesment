from selenium.webdriver.common.by import By
from POM.Base import Base
from selenium.common.exceptions import TimeoutException
from utility.CustomExceptions import PageNotLoadedException, CheckboxNotSelectedException


class Checkbox(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.elements_xpath = (By.XPATH, '//a[@href="/elements"]')
        self.elements_page_title = (By.XPATH, '//div[text()="Please select an item from left to start practice."]')
        self.check_box_xpath = (By.XPATH, '//span[text()="Check Box"]')
        self.check_box_title = (By.XPATH, '//h1[text()="Check Box"]')
        self.plus_icon_xpath = (By.XPATH, '//span[contains(@class, "rc-tree-switcher_close")]')
        self.tree_ele_xpath = (By.XPATH, '//div[@role="treeitem"]')
        self.indent_xpath = (By.XPATH, './span[@class="rc-tree-indent"]/span')
        self.leaf_check_status = (By.XPATH, './span[contains(@class, "rc-tree-checkbox")]')

    def navigate_to_checkbox(self):
        self.open_url()
        self.click_on_element(locator=self.elements_xpath)
        try:
            self.wait_till_visible(locator=self.elements_page_title, timeout=10, name='Element Page')
        except TimeoutException:
            raise PageNotLoadedException(msg='Elements page not loaded successfully..!')

        self.log.info('Successfully navigated to "Elements" page')

        self.click_on_element(locator=self.check_box_xpath)

        try:
            self.wait_till_visible(locator=self.check_box_title, timeout=10, name='Checkbox Page')
        except TimeoutException:
            raise PageNotLoadedException(msg='Checkbox page not loaded successfully..!')
        self.log.info('Successfully navigated to "Checkbox" page')

    def expand_tree(self):
        self.log.info('Expanding all the checkbox tree')
        tree = self.driver.find_elements(*self.plus_icon_xpath)
        while tree:
            for ele in tree:
                ele.click()
            tree = self.driver.find_elements(*self.plus_icon_xpath)
        self.log.info('Successfully expanded')

    def tick_checkbox(self, name):
        self.log.info(f'Clicking on the checkbox -> {name}')
        locator = (By.XPATH, f'//span[contains(@aria-label, "{name}")]')
        self.click_on_element(locator=locator)
        if self.driver.find_element(*locator).get_attribute('aria-checked') == 'true':
            self.log.info(f'Checkbox -> {name} clicked successfully')
        else:
            raise CheckboxNotSelectedException(msg=f'After clicking checkbox -> {name}, check status is false')

    def __get_tree_structure(self):
        self.log.info('Fetching entire checkbox tree structure')
        return [(len(ele.find_elements(*self.indent_xpath)), ele) for ele in self.driver.find_elements(*self.tree_ele_xpath)]

    def get_check_leaf_result(self, parent_node):
        self.log.info(f'Fetching leaf nodes check status under parent -> {parent_node}')
        tree = self.__get_tree_structure()
        if not tree:
            raise ValueError('<ERROR>- Failed to fetch tree structure data')
        self.log.info('Successfully fetched tree structure data')
        result = []
        n = -1
        for ind, ele in tree:
            if ele.text == parent_node:
                n = ind
            elif n != -1 and n != ind:
                res = True if ele.find_element(*self.leaf_check_status).get_attribute('aria-checked') == 'true' else False
                result.append(res)
            elif n != -1 and n == ind:
                break
        return result

