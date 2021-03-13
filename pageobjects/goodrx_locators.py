""" Created by Alysha Kester-Terry 3/12/2021
    This Base Page object locator strategy was gleaned with much gratitude from
    http://elementalselenium.com/tips/9-use-a-base-page-object in October 2020
"""
from selenium.webdriver import ActionChains

from LocatorsUtil import BaseLocators, wait_for_seconds


class BasePageLocators(BaseLocators):
    """Initializes the driver for use on all other pages and defines objects that are on almost every page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


class SearchPageLocators(BasePageLocators):
    """Locators on the Search Page. Inherit any base page locators if there are any. Automatically inherits
    BaseLocators """

    def robot_killer(self):
        element = BaseLocators.element_by_xpath(self, '//*[@id="px-captcha"]/iframe', 5)
        if element:
            action = ActionChains(self.driver)
            print('Clicking and holding on element...')
            action.click_and_hold(on_element=element)
            action.perform()
            wait_for_seconds(2)
            action.release()
            action.perform()

    def search_field(self):
        return BaseLocators.element_by_css(self, "[data-qa='search-inp']")

    def get_result_list(self):
        return BaseLocators.elements_by_css(self, "aria-selected")


class PricePageLocators(BasePageLocators):
    """Locators on the Price Page. Inherit any base page locators if there are any. Automatically inherits
    BaseLocators """

    def compare_prices_popup_content(self):
        return BaseLocators.elements_by_classname(self, 'tooltipContent-3F-5e')

    def compare_prices_popup_dismiss(self):
        return BaseLocators.element_by_xpath(self, ".//button[contains(text(),'OK')]")

    def rx_settings_panel(self):
        return BaseLocators.element_by_css(self, "[data-qa='prescription_settings_ctn']")

    def price_rows(self):
        return BaseLocators.elements_by_css(self, "[data-qa='price_row']")

    def store_names(self):
        return BaseLocators.elements_by_css(self, "[data-qa='store_name']")

    def drug_prices(self):
        return BaseLocators.elements_by_css(self, "[data-qa='drug_price']")

    def nested_row_button(self, element):
        return BaseLocators.nested_element_by_css(self, element, "[data-qa='coupon_button']")


class CouponPageLocators(BasePageLocators):
    """Coupon page locators"""

    def popup_closure(self):
        return BaseLocators.element_by_css(self, "[data-qa='gold-icoupon-close']", 5)

    def clipping(self):
        return BaseLocators.element_by_css(self, "[data-qa='clipping']")

    def price(self):
        return BaseLocators.element_by_css(self,"[data-qa='coupon_price']")

    def store_name(self):
        return BaseLocators.element_by_css(self,"[data-qa='coupon_pharmacy_name']")