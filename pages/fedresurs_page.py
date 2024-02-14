import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FedresursPage(BasePage):
    UNIQUE_LOCATOR = (By.CSS_SELECTOR, "fedresurs-app")

    def open(self):
        self.open_page(FedresursPage.UNIQUE_LOCATOR)

    #
    @allure.step
    def is_page_loaded(self):
        try:
            self.find(self.UNIQUE_LOCATOR)
            return True
        except TimeoutException:
            raise AssertionError(
                f"Not found unique locator: {self.UNIQUE_LOCATOR}")


class SearchBiddingPage(FedresursPage):
    UNIQUE_LOCATOR = (By.CSS_SELECTOR, "fedresurs-app search bidding-search")


class MonitoringPage(FedresursPage):
    UNIQUE_LOCATOR = (By.CSS_SELECTOR, "fedresurs-app monitoring")


class NewsPage(FedresursPage):
    UNIQUE_LOCATOR = (By.CSS_SELECTOR, "fedresurs-app news")


class AboutProjectPage(FedresursPage):
    UNIQUE_LOCATOR = (By.CSS_SELECTOR, "fedresurs-app about")


class HelpPage(FedresursPage):
    UNIQUE_LOCATOR = (By.CSS_SELECTOR, "fedresurs-app help")
