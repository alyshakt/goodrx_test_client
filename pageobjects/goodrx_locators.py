""" Created by Alysha Kester-Terry 3/12/2021
    This Base Page object locator strategy was gleaned with much gratitude from
    http://elementalselenium.com/tips/9-use-a-base-page-object in October 2020
"""
from selenium.webdriver import ActionChains

from LocatorsUtil import BaseLocators


class BasePageLocators(BaseLocators):
    """Initializes the driver for use on all other pages and defines objects that are on almost every page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


class SearchPageLocators(BasePageLocators):
    """Inherit any base page locators if there are any. Automatically inherits BaseLocators"""

    def robot_killer(self):
        element = BaseLocators.element_by_xpath(self, '//*[@id="px-captcha"]/iframe', 5)
        if element:
            action = ActionChains(self.driver)
            print('Clicking and holding on element...')
            action.click_and_hold(on_element=element)
            action.perform()
            self.sleep_time(2)
            action.release()
            action.perform()


    def search_field(self):
        return BaseLocators.element_by_css(self, "[data-qa='search-inp']")

    def get_result_list(self):
        return BaseLocators.elements_by_css(self, "aria-selected")
