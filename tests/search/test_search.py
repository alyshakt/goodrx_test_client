from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from page_objects.goodrx.pages import BasePage, SearchPage
from setup.SetupEnvironment import Environment, SetupEnvironment


def test_search(record_xml_attribute):
    record_xml_attribute('name', 'GoodRx Test Project Test 1')
    fail = None
    env = Environment.goodrx
    # Setup Driver, define options
    options = FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    search_page = SearchPage(driver)
    base_page = BasePage(driver)
    #
    search_term = 'Amoxicillin'
    # Define the Search page and the page objects
    SetupEnvironment.navigate_to_environment(driver=driver, Environment=env)
    search_page.enter_search_text(search_term)
