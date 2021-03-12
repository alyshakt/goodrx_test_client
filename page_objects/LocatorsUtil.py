# Define the default wait factor. I like doing between ~30-45 seconds especially to allow for page loading
import time
import logging
from selenium.common.exceptions import NoSuchElementException

default_wait = 45


def sleep_time(seconds_to_wait=5):
    """Hard sleep if absolutely needed. Defaults to 5 seconds"""
    time.sleep(seconds_to_wait)


class BaseLocators(object):
    """Initializes the driver for use on all other pages and defines objects that are on almost every page"""

    # Initialize the driver
    def __init__(self, driver):
        self.driver = driver

    """The following functions automatically search for an element by a given type of locator, with a wait for visibility
    These methods have 2 different outputs: 1) The element itself if it is found, or 2) The boolean value of False if it is not found.
    This is particularly helpful in asserting that an element exists.
    Each function allows for an explicit max wait time to be passed through as some elements may need extra care for loading
    """

    def element_by_classname(self, identifier, wait_time=default_wait):
        timestamp = int(time.time())
        try:
            exists = self.driver.find_element(By.CLASS_NAME, identifier)
        except NoSuchElementException as n:
            print('The element could not be found by ClassName: {}'.format(identifier))
            exists = False
        while exists is False and (int(time.time()) - timestamp) < wait_time:
            try:
                exists = bool(self.driver.find_element(By.CLASS_NAME, identifier))
                print('We found the element? {}'.format(exists))
            except NoSuchElementException as n:
                logging.warning('An exception was thrown!', exc_info=False)
            if exists:
                return exists
            else:
                print('Waiting for the element...')
                sleep_time(2)
        return exists

    def element_by_id(self, identifier, wait_time=default_wait):
        timestamp = int(time.time())
        try:
            exists = self.driver.find_element(By.ID, identifier)
        except NoSuchElementException as n:
            print('The element could not be found by ID: {}'.format(identifier))
            exists = False
        while exists is False and (int(time.time()) - timestamp) < wait_time:
            try:
                exists = bool(self.driver.find_element(By.ID, identifier))
                print('We found the element? {}'.format(exists))
            except NoSuchElementException as n:
                logging.warning('An exception was thrown!', exc_info=False)
            if exists:
                return exists
            else:
                print('Waiting for the element...')
                sleep_time(2)
        return exists

    def element_by_xpath(self, identifier, wait_time=default_wait):
        timestamp = int(time.time())
        try:
            exists = self.driver.find_element(By.XPATH, identifier)
        except NoSuchElementException as n:
            print('The element could not be found by XPath: {}'.format(identifier))
            exists = False
        while exists is False and (int(time.time()) - timestamp) < wait_time:
            try:
                exists = self.driver.find_element(By.XPATH, identifier)
                print('We found the element? {}'.format(exists))
            except NoSuchElementException as n:
                logging.warning('An exception was thrown!', exc_info=False)
            if exists:
                return exists
            else:
                print('Waiting for the element...')
                sleep_time(2)
        return exists

    def element_by_css(self, identifier, wait_time=default_wait):
        timestamp = int(time.time())
        try:
            exists = self.driver.find_element(By.CSS_SELECTOR, identifier)
        except NoSuchElementException as n:
            print('The element could not be found by ClassName: {}'.format(identifier))
            exists = False
        while exists is False and (int(time.time()) - timestamp) < wait_time:
            try:
                exists = self.driver.find_element(By.CSS_SELECTOR, identifier)
                print('We found the element? {}'.format(exists))
            except NoSuchElementException as n:
                logging.warning('An exception was thrown!', exc_info=False)
            if exists:
                return exists
            else:
                print('Waiting for the element...')
                sleep_time(2)
        return exists

    def elements_by_css(self, identifier, wait_time=default_wait):
        timestamp = int(time.time())
        try:
            exists = self.driver.find_elements(By.CSS_SELECTOR, identifier)
        except NoSuchElementException as n:
            print('The element could not be found by ClassName: {}'.format(identifier))
            exists = False
        while exists is False and (int(time.time()) - timestamp) < wait_time:
            try:
                exists = self.driver.find_elements(By.CSS_SELECTOR, identifier)
                print('We found the element? {}'.format(exists))
            except NoSuchElementException as n:
                logging.warning('An exception was thrown!', exc_info=False)
            if exists:
                return exists
            else:
                print('Waiting for the element...')
                sleep_time(2)
        return exists

    def elements_by_classname(self, identifier, wait_time=default_wait):
        timestamp = int(time.time())
        try:
            exists = self.driver.find_elements(By.CLASS_NAME, identifier)
        except NoSuchElementException as n:
            print('The element could not be found by ClassName: {}'.format(identifier))
            exists = False
        while exists is False and (int(time.time()) - timestamp) < wait_time:
            try:
                exists = self.driver.find_elements(By.CLASS_NAME, identifier)
                print('We found the element? {}'.format(exists))
            except NoSuchElementException as n:
                logging.warning('An exception was thrown!', exc_info=False)
            if exists:
                return exists
            else:
                print('Waiting for the element...')
                sleep_time(2)
        return exists

    def elements_by_id(self, identifier, wait_time=default_wait):
        timestamp = int(time.time())
        try:
            exists = self.driver.find_elements(By.ID, identifier)
        except NoSuchElementException as n:
            print('The element could not be found by ID: {}'.format(identifier))
            exists = False
        while exists is False and (int(time.time()) - timestamp) < wait_time:
            try:
                exists = self.driver.find_elements(By.ID, identifier)
                print('We found the element? {}'.format(exists))
            except NoSuchElementException as n:
                logging.warning('An exception was thrown!', exc_info=False)
            if exists:
                return exists
            else:
                print('Waiting for the element...')
                sleep_time(2)
        return exists

    def elements_by_xpath(self, identifier, wait_time=default_wait):
        timestamp = int(time.time())
        try:
            exists = self.driver.find_elements(By.XPATH, identifier)
        except NoSuchElementException as n:
            print('The element could not be found by XPath: {}'.format(identifier))
            exists = False
        while exists is False and (int(time.time()) - timestamp) < wait_time:
            try:
                exists = self.driver.find_elements(By.XPATH, identifier)
                print('We found the element? {}'.format(exists))
            except NoSuchElementException as n:
                logging.warning('An exception was thrown!', exc_info=False)
            if exists:
                return exists
            else:
                print('Waiting for the element...')
                sleep_time(2)
        return exists

    def element_by_name(self, identifier, wait_time=default_wait):
        timestamp = int(time.time())
        try:
            exists = self.driver.find_element(By.NAME, identifier)
        except NoSuchElementException as n:
            print('The element could not be found by name: {}'.format(identifier))
            exists = False
        while exists is False and (int(time.time()) - timestamp) < wait_time:
            try:
                exists = self.driver.find_element(By.NAME, identifier)
                print('We found the element? {}'.format(exists))
            except NoSuchElementException as n:
                logging.warning('An exception was thrown!', exc_info=False)
            if exists:
                return exists
            else:
                print('Waiting for the element...')
                sleep_time(2)
        return exists

    def elements_by_name(self, identifier, wait_time=default_wait):
        timestamp = int(time.time())
        try:
            exists = self.driver.find_elements(By.NAME, identifier)
        except NoSuchElementException as n:
            print('The element could not be found by name: {}'.format(identifier))
            exists = False
        while exists is False and (int(time.time()) - timestamp) < wait_time:
            try:
                exists = self.driver.find_elements(By.NAME, identifier)
                print('We found the element? {}'.format(exists))
            except NoSuchElementException as n:
                logging.warning('An exception was thrown!', exc_info=False)
            if exists:
                return exists
            else:
                print('Waiting for the element...')
                sleep_time(2)
        return exists
