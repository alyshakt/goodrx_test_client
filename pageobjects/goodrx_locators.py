""" Created by Alysha Kester-Terry 3/12/2021
    This Base Page object locator strategy was gleaned with much gratitude from
    http://elementalselenium.com/tips/9-use-a-base-page-object in October 2020
"""
from selenium.webdriver import ActionChains

from LocatorsUtil import BaseLocators, wait_for_seconds

default_wait = 45


class BasePageLocators(BaseLocators):
    """Initializes the driver for use on all other pages and defines objects that are on almost every page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def robot_killer(self):
        element = BaseLocators.element_by_xpath(self, '//*[@id="px-captcha"]/iframe', 5)
        if element:
            action = ActionChains(self.driver)
            print('Clicking and holding on element...')
            action.click_and_hold(on_element=element)
            action.perform()
            wait_for_seconds(3)
            action.release()
            action.perform()

    def popups(self):
        gold = BaseLocators.element_by_css(self, "[data-qa='gold-icoupon-close']", 3)
        newsletter = BaseLocators.element_by_css(self, "[data-qa='modal_close_btn_newsletter-modal-redesign']", 3)
        otcheader = BaseLocators.element_by_classname(self, 'modalHeader-V4_zF', 3)
        otc_restrictions = False
        if otcheader:
            otc_restrictions = BaseLocators.nested_element_by_css(self, otcheader, 'icon-close-UX5U5', 1)
        return gold, newsletter, otc_restrictions


class SearchPageLocators(BasePageLocators):
    """Locators on the Search Page. Inherit any base page locators if there are any. Automatically inherits
    BaseLocators """

    def search_field(self):
        return BaseLocators.element_by_css(self, "[data-qa='search-inp']")

    def get_result_list(self):
        return BaseLocators.elements_by_css(self, "aria-selected")

    def drug_title(self):
        return BaseLocators.element_by_id(self, 'uat-drug-title')


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

    def pharmacy_names(self):
        return BaseLocators.elements_by_css(self, "[data-qa='store_name']")

    def drug_prices(self):
        return BaseLocators.elements_by_css(self, "[data-qa='drug_price']")

    def nested_row_button(self, element):
        return BaseLocators.nested_element_by_css(self, element, "[data-qa='coupon_button']")


class CouponPageLocators(BasePageLocators):
    """Coupon page locators"""

    def clipping(self):
        return BaseLocators.element_by_css(self, "[data-qa='clipping']")

    def price_info_section(self):
        return BaseLocators.element_by_css(self, "[data-qa='coupon_content_price_info']")

    def price(self):
        return BaseLocators.element_by_css(self, "[data-qa='coupon_price']", (default_wait / 3))

    def pharmacy_name(self):
        return BaseLocators.element_by_css(self, "[data-qa='coupon_pharmacy_name']", (default_wait / 3))

    def indexed_prices(self):
        element = BaseLocators.element_by_css(self, "[data-qa='coupon_content_price_info']", (default_wait / 3))
        return BaseLocators.nested_elements_by_css(self, element, 'div > span:nth-child(1)')

    def indexed_pharmacies(self):
        element = BaseLocators.element_by_css(self, "[data-qa='coupon_content_price_info']", (default_wait / 3))
        return BaseLocators.nested_elements_by_css(self, element, 'div > span:nth-child(2)')
