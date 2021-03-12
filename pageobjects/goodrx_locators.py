""" Created by Alysha Kester-Terry 3/12/2021
    This Base Page object locator strategy was gleaned with much gratitude from
    http://elementalselenium.com/tips/9-use-a-base-page-object in October 2020
"""
from tests.LocatorsUtil import BaseLocators


class BasePageLocators(BaseLocators):
    """Initializes the driver for use on all other pages and defines objects that are on almost every page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


class SearchPageLocators(BasePageLocators):
    """Inherit any base page locators if there are any. Automatically inherits BaseLocators"""

    def search_field(self):
        return BasePageLocators.element_by_classname(self, "XCUIElementTypeTabBar")
