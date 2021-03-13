import datetime


def take_screenshot(driver, name=None):
    created_date = str(datetime.datetime.utcnow().strftime("%m-%d-%H%M"))
    add_name = str(name).replace(' ', '')
    file_name = 'test-reports/screenshots/{}{}.png'.format(add_name, created_date)
    print('Saving screenshot to {}'.format(file_name))
    driver.save_screenshot(file_name)
