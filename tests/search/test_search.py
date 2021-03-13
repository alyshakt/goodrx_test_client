from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import screenshot_util
from pageobjects.goodrx_pages import SearchPage, BasePage
from setup_environments.Environment import Environment
from setup_environments.EnvironmentSetup import navigate_to_environment


def test_search(record_xml_attribute):
    """Type "Amoxicillin" into the home page and select the first result in the
suggestions dropdown that appears."""
    record_xml_attribute('name', 'GoodRx Test Project Test 1')
    fail = None
    # Setup Driver, define options
    options = Options()
    options.add_argument("disable-popup-blocking")
    options.add_argument("enable-javascript")
    options.add_argument("disable-extensions")
    # options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)

    search_page = SearchPage(driver)
    base_page = BasePage(driver)
    #
    search_term = 'Amoxicillin'
    # Define the Search page and the page objects
    try:
        navigate_to_environment(driver=driver, Environment=Environment.goodrx)
        assert search_page.page_initiated()
        search_page.enter_search_text(search_term)
        screenshot_util.take_screenshot(driver, search_term)
        search_page.select_first_result()
        base_page.sleep_time(2)
    except (BaseException, Exception) as failure:
        fail = failure
        print('!!!!! The test failed. {}'.format(fail))
        base_page.process_failure(fail)
    finally:
        # Finally, quit the driver and appium service!
        base_page.tear_down(fail)
