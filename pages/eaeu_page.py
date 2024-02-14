import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class EaeuPage(BasePage):
    UNIQUE_LOCATOR = (By.CSS_SELECTOR, "app-root app-eaeu")

    def open(self):
        self.open_page(EaeuPage.UNIQUE_LOCATOR)

    #
    @allure.step
    def is_page_loaded(self):
        try:
            self.find(self.UNIQUE_LOCATOR)
            return True
        except TimeoutException:
            raise AssertionError(
                f"Not found unique locator: {self.UNIQUE}")
