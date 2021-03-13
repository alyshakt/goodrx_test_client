from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pageobjects.goodrx_pages import SearchPage, BasePage, PricePage, CouponPage
from setup_environments.Environment import Environment
from setup_environments.EnvironmentSetup import navigate_to_environment


def test_search(record_xml_attribute):
    """Verify that prices found on the Price Page with discount offers match prices found on their respective store pages
        Verify that store names are also matched
        """
    record_xml_attribute('name', 'GoodRx Test Project Test 1')
    fail = None
    # Setup Driver, define options
    options = Options()
    options.add_argument("disable-popup-blocking")
    options.add_argument("enable-javascript")
    options.add_argument("disable-extensions")
    # options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)
    base_page = BasePage(driver)
    search_page = SearchPage(driver)
    price_page = PricePage(driver)
    coupon_page = CouponPage(driver)

    #
    search_term = 'Amoxicillin'
    # Define the Search page and the page objects
    try:
        navigate_to_environment(driver=driver, Environment=Environment.goodrx)
        assert search_page.page_initiated()
        search_page.enter_search_text(search_term)
        base_page.save_screenshot(search_term)
        search_page.select_first_result()
        assert price_page.page_initiated()
        assert price_page.settings_panel_exists()
        #For each price row with a Get Free Coupon or Get Free Discount,
        # Click on the button and
        # verify that the price on the price row matches the one shown on the new page,
        # and the store name matches.
        assert price_page.price_rows_exist()
        assert price_page.count_of_price_rows() > 0
        stores_and_prices = price_page.get_stores_and_prices()
        for result in stores_and_prices:
            this_result = result['storePrice']
            if 'coupon' in this_result['priceType']:
                store = this_result['store']
                store_price = this_result['price']
                price_page.click_result_matching(store)
                base_page.wait_for_seconds(5)
                base_page.switch_tab()
                base_page.save_screenshot('resultclicked')
                assert coupon_page.page_initiated()
                price_found = coupon_page.get_price().replace('$')
                store_name = coupon_page.get_store_name().lower()
                assert store_name == store.lower()
                assert price_found == store_price
                base_page.switch_tab()

                # base_page.navigate_back()

    except (BaseException, Exception) as failure:
        fail = failure
        print('!!!!! The test failed. {}'.format(fail))
        base_page.process_failure(fail)
    finally:
        # Finally, quit the driver and appium service!
        base_page.tear_down(fail)
