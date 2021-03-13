"""Created by Alysha Kester-Terry 3/12/2021"""
import datetime
import logging
import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from pageobjects.goodrx_locators import SearchPageLocators


class BasePage(object):
    """Base page class to initialize the page class that will be called from all pages"""

    def __init__(self, driver):
        """Initialize the driver"""
        self.driver = driver

    def sleep_time(self, seconds_to_wait=5):
        """Hard sleep if absolutely needed. Defaults to 5 seconds"""
        time.sleep(seconds_to_wait)

    def take_screenshot(self, name=None):
        """A screenshot util to take screenshots and save them to a test-reports folder inclusive of timestamp
        and able to take an explicit file name value"""
        created_date = str(datetime.datetime.utcnow().strftime("%m-%d-%H%M"))
        add_name = str(name).replace(' ', '')
        file_name = './test-reports/screenshots/' + add_name + created_date + '.png'
        print('Saving screenshot to {}'.format(file_name))
        self.driver.save_screenshot(file_name)

    # Functional/Interaction with Page Elements
    def enter_text(self, element, text_to_enter):
        """Enter text into an element"""
        element.clear()
        element.send_keys(text_to_enter)

    def get_element_text(self, element):
        """Get an element's text"""
        return element.text

    def scroll_to_element(self, element):
        """Click an element by a defined locator"""
        coordinates = element.location_once_scrolled_into_view  # returns dict of X, Y coordinates
        self.driver.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))

    def click_element(self, element):
        """Click an element"""
        element.click()

    def get_page_src_info(self):
        """Get a page source output"""
        source_hierarchy = self.driver.page_source
        return str(source_hierarchy)

    def process_failure(self, error):
        """process a test failure, print the page source and fail the test"""
        print(self.get_page_src_info())
        pytest.fail('The test failed. {}'.format(error), True)

    def tear_down(self, failure):
        """If there was a failure, capture the moment the failure occurred, otherwise capture the pass, and quit the driver."""
        if failure is None:
            self.take_screenshot('Pass')
        else:
            self.take_screenshot('Failed')
        self.driver.quit()


class SearchPage(BasePage):
    """Inherit all the base page capabilities"""

    def page_initiated(self):
        SearchPageLocators.robot_killer(self)
        return bool(SearchPageLocators.search_field(self))

    def enter_search_text(self, text_to_enter):
        try:
            element = SearchPageLocators.search_field(self)
            self.enter_text(element, text_to_enter)
        except(AttributeError):
            logging.warning('The element was not found.', exc_info=True)

    def select_first_result(self):
        self.sleep_time(2)
        element = SearchPageLocators.search_field(self)
        element.send_keys(Keys.RETURN)

    def get_list_options(self):
        element_list = SearchPageLocators.get_result_list(self)
        for element in element_list:
            print(self.get_element_text(element))

    def wait_for_seconds(self, int):
        self.sleep_time(int)
