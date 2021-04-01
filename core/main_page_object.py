import selenium.common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPageObject:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_present(self, locator: str, error_message: str, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(
                EC.presence_of_element_located(
                    MainPageObject._get_tuple_by_locator(locator)
                )
            )
        except selenium.common.exceptions.TimeoutException:
            print(error_message)

    def wait_for_elements_present(self, locator: str, error_message: str, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(
                EC.presence_of_all_elements_located(
                    MainPageObject._get_tuple_by_locator(locator)
                )
            )
        except selenium.common.exceptions.TimeoutException:
            print(error_message)

    def wait_for_alert_present(self, error_message: str = "Alert is not present", timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.alert_is_present())
        except selenium.common.exceptions.TimeoutException:
            print(error_message)

    def get_element(self, locator: str, error_message: str):
        try:
            return self.driver.find_element(MainPageObject._get_tuple_by_locator(locator)[0],
                                            MainPageObject._get_tuple_by_locator(locator)[1])
        except selenium.common.exceptions.TimeoutException:
            print(error_message)

    @staticmethod
    def _get_tuple_by_locator(locator):
        if ':' not in locator:
            raise Exception(f'Locator w/o a type: {locator}')

        split_locator = locator.split(':', 1)
        type_of_locator = split_locator[0]
        pure_locator = split_locator[1]

        if type_of_locator == 'css':
            by = By.CSS_SELECTOR
        elif type_of_locator == 'id':
            by = By.ID
        elif type_of_locator == 'xpath':
            by = By.XPATH
        else:
            raise Exception(f'Cannot detect locator type {type_of_locator}. Full locator {locator}')

        return by, pure_locator

