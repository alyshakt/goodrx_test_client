from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_search(record_xml_attribute):
    record_xml_attribute('name', 'GoodRx Test Project Test 1')
    fail = None
    env = Environment.goodrx
    # Setup Driver, define options
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)
    search_page = SearchPage(driver)
    base_page = BasePage(driver)
    #
    search_term = 'Amoxicillin'
    # Define the Search page and the page objects
    SetupEnvironment.navigate_to_environment(driver=driver, Environment=env)
    search_page.enter_search_text(search_term)
