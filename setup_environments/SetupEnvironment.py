"""Created by Alysha Kester-Terry 3/12/2021 for GoodRx
This file is to set up the driver for a specific site.
We want to make this scalable in case there could be multiple environments or web UI URLs we may want to hit.
"""
import enum


class Environment(enum.Enum):
    """To standardize environment input and reduce human error"""
    goodrx = 1


class SetupEnvironment(Environment):

    def get_app_url(self, Environment):
        """To define the environments / URLs we want to hit"""
        switcher = {
            Environment.goodrx: 'https://goodrx.com/'
        }
        env = switcher.get(Environment, 'Invalid environment option, or not yet implemented')
        print(env)
        return env

    def navigate_to_environment(self, driver, Environment):
        """To navigate to the appropriate URL"""
        url = self.get_app_url(Environment)
        driver.get(url)
        link = driver.current_url
        print('The current url is: {}'.format(link))
