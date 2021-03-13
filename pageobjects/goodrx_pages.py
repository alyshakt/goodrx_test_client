"""Created by Alysha Kester-Terry 3/12/2021"""
import logging

import pytest
from selenium.webdriver.common.keys import Keys

import LocatorsUtil
import screenshot_util
from LocatorsUtil import wait_for_seconds
from pageobjects.goodrx_locators import SearchPageLocators, PricePageLocators, CouponPageLocators


class BasePage(object):
    """Base page class to initialize the page class that will be called from all pages"""

    def __init__(self, driver):
        """Initialize the driver"""
        self.driver = driver

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

    def get_tabs(self):
        print("Parent window title: " + self.driver.title)
        # get current window handle
        parent_handle = self.driver.current_window_handle
        child_handles = None
        try:
            # from https://www.browserstack.com/guide/how-to-switch-tabs-in-selenium-python

            # get first child window
            child_handles = self.driver.window_handles
        except (BaseException, Exception) as n:
            logging.warning('An exception occurred: {}'.format(n), True)
        return parent_handle, child_handles

    def close_child_tabs(self):
        parent, children = self.get_tabs()
        for child in children:
            if child != parent:
                self.driver.switch_to.window(child)
                self.driver.close()
        self.driver.switch_to.window(parent)

    def switch_tab(self):
        parent, children = self.get_tabs()
        for child in children:
            if child != parent:
                self.driver.switch_to.window(child)
                break

    def click_element(self, element):
        """Click an element"""
        element.click()

    def save_screenshot(self, name=None):
        screenshot_util.take_screenshot(self.driver, name)

    def tear_down(self, failure):
        if failure is None:
            self.save_screenshot('Pass')
        else:
            self.save_screenshot('Failed')
        self.driver.quit()

    def get_page_src_info(self):
        source_hierarchy = self.driver.page_source
        return str(source_hierarchy)

    def process_failure(self, error):
        print(self.get_page_src_info())
        pytest.fail('The test failed. {}'.format(error), True)

    def navigate_back(self):
        self.driver.back()

    def wait_for_seconds(self, int):
        LocatorsUtil.wait_for_seconds(int)

    def refresh_screen(self):
        self.driver.refresh()


class SearchPage(BasePage):
    """Search Page: Inherit all the base page capabilities"""

    def page_initiated(self):
        SearchPageLocators.robot_killer(self)
        self.save_screenshot('SearchPage')
        return bool(SearchPageLocators.search_field(self))

    def enter_search_text(self, text_to_enter):
        try:
            element = SearchPageLocators.search_field(self)
            self.enter_text(element, text_to_enter)
        except AttributeError:
            logging.warning('Search field was not found...', exc_info=True)

    def select_first_result(self):
        wait_for_seconds(2)
        element = SearchPageLocators.search_field(self)
        self.save_screenshot('FirstResult')
        element.send_keys(Keys.RETURN)


class PricePage(BasePage):
    """Price Page: Inherit all the base page capabilities"""

    def page_initiated(self):
        element = PricePageLocators.rx_settings_panel(self)
        self.save_screenshot('PricePage')
        return bool(element)

    def settings_panel_exists(self):
        return bool(PricePageLocators.rx_settings_panel(self))

    def price_rows_exist(self):
        return bool(PricePageLocators.price_rows(self))

    def count_of_price_rows(self):
        return len(PricePageLocators.price_rows(self))

    def get_price_row_data(self):
        elements = PricePageLocators.price_rows(self)
        rows_data = list()
        for name in elements:
            rows_data.append(self.get_element_text(name))
        return rows_data

    def get_store_list(self):
        elements = PricePageLocators.store_names(self)
        store_list_names = list()
        for name in elements:
            prepped_name = self.get_element_text(name).split(':\n')[1].replace('\n.', '')
            if '\n' in prepped_name:
                prepped_name = prepped_name.split('\n')[0]
            store_list_names.append(prepped_name)
        return store_list_names

    def get_drug_prices(self):
        elements = PricePageLocators.drug_prices(self)
        drug_price_data_dict = []
        for price_data in elements:
            raw_string = self.get_element_text(price_data)
            print(raw_string)
            split_data = raw_string.split('$')
            price_type = split_data[0]
            if 'retail' in price_type:
                price_type = 'retail'
            if 'coupon' in price_type:
                price_type = 'coupon'
            price = split_data[1]
            if '\n' in price:
                price = price.split('\n')[0]
            drug_price_data_dict.append({"prices": {
                "price": price,
                "priceType": price_type
            }
            })
        print('{}'.format(drug_price_data_dict))
        return drug_price_data_dict

    def get_stores_and_prices(self):
        final_data_dict = []
        stores = PricePageLocators.store_names(self)
        drug_prices = PricePageLocators.drug_prices(self)
        assert len(stores) == len(drug_prices)
        for index in range(len(stores)):
            prepped_store_name = self.get_element_text(stores[index]).split(':\n')[1].replace('\n.', '')
            if '\n' in prepped_store_name:
                prepped_store_name = prepped_store_name.split('\n')[0]
            price_data = drug_prices[index]
            raw_string = self.get_element_text(price_data)
            split_data = raw_string.split('$')
            price_type = split_data[0]
            if 'retail' in price_type:
                price_type = 'retail'
            if 'coupon' in price_type:
                price_type = 'coupon'
            price = split_data[1]
            if '\n' in price:
                price = price.split('\n')[0]
            final_data_dict.append({"storePrice": {
                "store": prepped_store_name,
                "price": price,
                "priceType": price_type
            }})
            index += 1
        print('Final data found: {}'.format(final_data_dict))
        return final_data_dict

    def click_result_matching(self, match_data):
        stores = PricePageLocators.store_names(self)
        drug_prices = PricePageLocators.drug_prices(self)
        price_rows = PricePageLocators.price_rows(self)

        for row in range(len(price_rows)):
            this_row = price_rows[row]
            store = stores[row]
            price = drug_prices[row]
            store_info = self.get_element_text(store)
            price_info = self.get_element_text(price)
            info_button = PricePageLocators.nested_row_button(self, this_row)
            if match_data in store_info or match_data in price_info:
                print('Found matching result {}{} at index {}'.format(store_info, price_info, row))
                self.scroll_to_element(this_row)
                self.click_element(info_button)
                self.save_screenshot(match_data)


class CouponPage(BasePage):
    """Coupon Page actions"""

    def page_initiated(self):
        popup = CouponPageLocators.popup_closure(self)
        if popup:
            self.click_element(popup)
        self.save_screenshot('couponpage')
        return bool(CouponPageLocators.clipping(self))

    def get_price(self):
        element = CouponPageLocators.price(self)
        prices = CouponPageLocators.indexed_prices(self)
        price_text_list = []
        if element:
            price_text_list.append(self.get_element_text(element).replace('$', ''))
        else:
            for price in prices:
                price_text_list.append(self.get_element_text(price).replace('$', '') + ' or ')
        return ''.join(price_text_list)

    def get_store_name(self):
        element = CouponPageLocators.store_name(self)
        return self.get_element_text(element).replace('at ', '')
