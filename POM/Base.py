from selenium.webdriver.support.ui import Select
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.ReadJson import ReadJson
from selenium.webdriver import ActionChains
from utility.Log import get_logger
import matplotlib.colors as mcolors


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.log = get_logger(__name__)
        self.read_json = ReadJson()
        self.actions = ActionChains(driver)
        self.home_page_xpath = (By.XPATH, '//div[@class="category-cards"]')

    def open_url(self):
        url = self.read_json.get_data('url')
        self.log.info(f'Opening url: {url}')
        self.driver.get(url)
        self.wait_till_visible(locator=self.home_page_xpath, timeout=10, name=url)

    def __wait_setup(self, timeout):
        wait = WebDriverWait(self.driver, timeout)
        return wait

    def wait_till_visible(self, locator, timeout, name):
        wait = self.__wait_setup(timeout)
        self.log.info(f'Waiting {timeout} seconds for {name} visibility')
        wait.until(EC.visibility_of_element_located(locator))

    def click_on_element(self, locator):
        max_try = 10
        while max_try > 0:
            try:
                element = self.driver.find_element(*locator)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                self.wait_till_element_clickable(locator=locator, timeout=10)
                element.click()
                break
            except ElementClickInterceptedException:
                max_try -= 1

    def page_reload(self):
        self.driver.refresh()

    def wait_till_element_clickable(self, locator, timeout):
        wait = self.__wait_setup(timeout)
        self.log.info(f'Waiting {timeout} seconds for element click ability')
        wait.until(EC.element_to_be_clickable(locator))

    def fill_data(self, locator, data):
        self.click_on_element(locator=locator)
        field = self.driver.find_element(*locator)
        field.clear()
        field.send_keys(data)

    def select_option(self, locator, option):
        dropdown_element = self.driver.find_element(*locator)
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(str(option))

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def find_color(self, rgba_color):
        rgba_value = rgba_color
        r, g, b = [int(float(x)) for x in rgba_value.strip("rgba()").split(",")][:3]

        # Convert to hex
        hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)

        # Find closest named color
        closest_name = min(mcolors.CSS4_COLORS, key=lambda name:
            sum((mcolors.to_rgb(mcolors.CSS4_COLORS[name])[i] - (r/255, g/255, b/255)[i])**2 for i in range(3))
        )
        return closest_name

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
