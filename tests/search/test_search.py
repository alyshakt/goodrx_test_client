from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page_objects.goodrx_pages import SearchPage, BasePage
from setup_environments.Environment import Environment
from setup_environments.EnvironmentSetup import navigate_to_environment


def test_search(record_xml_attribute):
    record_xml_attribute('name', 'GoodRx Test Project Test 1')
    fail = None
    # Setup Driver, define options
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)
    search_page = SearchPage(driver)
    base_page = BasePage(driver)
    #
    search_term = 'Amoxicillin'
    # Define the Search page and the page objects
    navigate_to_environment(driver=driver, Environment=Environment.goodrx)
    search_page.enter_search_text(search_term)
