import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pageobjects.goodrx_pages import SearchPage, BasePage, PricePage, CouponPage
from setup_environments.App import App
from setup_environments.AppSetup import navigate_to_environment


def test_search_advil_otc(environment, record_xml_attribute):
    #TODO
    """When searching for an OTC like Advil, Verify that prices found on the Price Page with discount offers match prices found on their respective store pages
        Verify that store names are also matched.
        """
    record_xml_attribute('name', 'GoodRx Test Project User Search -> OTC Coupon Workflow')
    fails = list()
    fail_text = None
    # Setup Driver, define options - Ideally put this in a more dynamic situation so you could pass arguments
    # to define these. But this does the job.
    options = Options()
    options.add_argument("headless")
    options.add_argument("disable-popup-blocking")
    options.add_argument("enable-javascript")
    options.add_argument("disable-extensions")
    driver = webdriver.Chrome(chrome_options=options)
    base_page = BasePage(driver)
    search_page = SearchPage(driver)
    price_page = PricePage(driver)
    coupon_page = CouponPage(driver)

    # TODO take into account differences in OTC, Controlled or specialty Rx Types.
    # Until then, expect failures here for Vicodin and Advil
    search_terms = ['Advil', 'True Metrix']
    try:
        for term in search_terms:
            try:
                print('There are {} search terms we will check'.format(len(search_terms)))
                navigate_to_environment(driver=driver, App=App.goodrx, environment=environment)
                assert search_page.page_initiated()
                search_page.enter_search_text(term)
                base_page.save_screenshot(term)
                search_page.select_first_result()
                assert price_page.page_initiated()
                assert term.lower() in price_page.get_drug_title().lower()
                assert price_page.settings_panel_exists()
                # For each price row with a Get Free Coupon or Get Free Discount, Click on the button and
                # verify that the price on the price row matches the one shown on the new page, and the pharmacy name matches.
                assert price_page.price_rows_exist()
                assert price_page.count_of_price_rows() > 0
                pharmacies_and_prices = price_page.get_pharmacies_and_prices()
                for result in pharmacies_and_prices:
                    this_result = result['pharmacyPrices']
                    if 'coupon' in this_result['priceType']:
                        print('Testing result: {}'.format(this_result))
                        pharmacy = this_result['pharmacy'].lower()
                        pharmacy_price = this_result['price']
                        assert price_page.click_result_matching(pharmacy)
                        base_page.wait_for_seconds(5)
                        base_page.switch_tab()
                        assert coupon_page.page_initiated()
                        price_found = coupon_page.get_price()
                        pharmacy_found = coupon_page.get_pharmacy_name()
                        assert pharmacy in ''.join(pharmacy_found)
                        assert pharmacy_price in ''.join(price_found)
                        base_page.switch_tab()
                        base_page.close_child_tabs()
                        base_page.wait_for_seconds(2)
                    else:
                        logging.info('Skipping non-coupon results: {}'.format(this_result))
            except (Exception, BaseException, AssertionError) as failure:
                fails.append(failure)
    except (Exception, BaseException) as failure:
        fails.append(failure)
        fail_text = ';'.join(fails)
        logging.error(msg=fail_text)
    finally:
        # Finally, quit the driver.
        base_page.tear_down(fail_text)
