"""Created by Alysha Kester-Terry 3/12/2021 for GoodRx
This file is to set up the driver for a specific site.
We want to make this scalable in case there could be multiple environments or web UI URLs we may want to hit.
"""


def get_app_url(App, environment='dev'):
    """To define the environments / URLs we want to hit
    :param environment:
    """
    if 'dev' in environment:
        env = '.dev.'
    else:
        env = ''
    switcher = {
        App.goodrx: 'goodrx.com/'
    }
    app_type = switcher.get(App, 'Invalid environment option, or not yet implemented')
    env_url = 'https://{}{}'.format(env, app_type)
    print(env_url)
    return env_url


def navigate_to_environment(driver, App, environment='dev'):
    """To navigate to the appropriate URL
    :param environment:
    """
    url = get_app_url(App, environment)
    driver.get(url)
    link = driver.current_url
    print('The current url is: {}'.format(link))
