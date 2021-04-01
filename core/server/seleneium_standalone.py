import os
from selenium import webdriver


class SeleniumStandalone:
    selenium_url = ""

    platform_map = ['chrome', 'chrome-headless', 'firefox', 'firefox-headless', 'opera', 'safari', 'edge', 'ie']

    def get_driver(self):
        if self.is_chrome():
            driver = webdriver.Remote(self.selenium_url, self._get_caps_for_chrome())
            driver.maximize_window()
            return driver
        elif self.is_chrome_headless():
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-gpu")
            options.headless = True
            driver = webdriver.Remote(self.selenium_url, self._get_caps_for_chrome(), options=options)
            return driver
        elif self.is_firefox():
            driver = webdriver.Remote(self.selenium_url, self._get_caps_for_firefox())
            driver.maximize_window()
            return driver
        elif self.is_firefox_headless():
            options = webdriver.FirefoxOptions()
            options.headless = True
            driver = webdriver.Remote(self.selenium_url, self._get_caps_for_firefox(), options=options)
            return driver
        elif self.is_opera():
            driver = webdriver.Remote(self.selenium_url, self._get_caps_for_opera())
            driver.maximize_window()
            return driver
        elif self.is_safari():
            driver = webdriver.Remote(self.selenium_url, self._get_caps_for_safari())
            driver.maximize_window()
            return driver
        elif self.is_edge():
            driver = webdriver.Remote(self.selenium_url, self._get_caps_for_edge())
            driver.maximize_window()
            return driver
        elif self.is_ie():
            driver = webdriver.Remote(self.selenium_url, self._get_caps_for_ie())
            driver.maximize_window()
            return driver
        else:
            raise Exception(f"Cannot get driver for ENV {self.get_platform_val()}")

    def is_chrome(self):
        return self.get_platform_val() == 'chrome'

    def is_chrome_headless(self):
        return self.get_platform_val() == 'chrome-headless'

    def is_firefox(self):
        return self.get_platform_val() == 'firefox'

    def is_firefox_headless(self):
        return self.get_platform_val() == 'firefox-headless'

    def is_opera(self):
        return self.get_platform_val() == 'opera'

    def is_safari(self):
        return self.get_platform_val() == 'safari'

    def is_edge(self):
        return self.get_platform_val() == 'edge'

    def is_ie(self):
        return self.get_platform_val() == 'ie'

    def get_platform_val(self):
        if 'platform' not in os.environ:
            raise Exception('Please, set ENV "platform"')

        env = os.environ['platform']

        if env not in self.platform_map:
            raise Exception(f"Unknown value of ENV 'platform'. Known list: {', '.join(self.platform_map)}. Got: {env}")

        return env

    def _get_caps_for_chrome(self):
        return webdriver.DesiredCapabilities.CHROME

    def _get_caps_for_firefox(self):
        return webdriver.DesiredCapabilities.FIREFOX

    def _get_caps_for_opera(self):
        return webdriver.DesiredCapabilities.OPERA

    def _get_caps_for_safari(self):
        return webdriver.DesiredCapabilities.SAFARI

    def _get_caps_for_edge(self):
        return webdriver.DesiredCapabilities.EDGE

    def _get_caps_for_ie(self):
        pass
