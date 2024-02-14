import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class MainPage(BasePage):
    """ Locators """
    UNIQUE_LOCATOR = (By.CSS_SELECTOR, "body app-root")

    SUPPORT_EMAIL = (By.CSS_SELECTOR, "header .mail a.mail__adr")
    SUPPORT_PHONES = (By.CSS_SELECTOR, "header .phone div.phone__block")

    """ Links """
    FEDRESURS_LINK = (
        By.CSS_SELECTOR, "header app-navigation li:nth-of-type(1) a")
    BIDDING_LINK = (By.CSS_SELECTOR,
                    "header app-navigation li:nth-of-type(2) a")
    EAEU_LINK = (By.CSS_SELECTOR, "app-header-bottom li:nth-of-type(3) a")
    MONITORING_LINK = (By.CSS_SELECTOR,
                       "app-header-bottom li:nth-of-type(4) a")
    NEWS_LINK = (By.CSS_SELECTOR, "app-header-bottom li:nth-of-type(5) a")
    ABOUT_PROJECT_LINK = (By.CSS_SELECTOR,
                          "app-header-bottom li:nth-of-type(6) a")
    HELP_LINK = (By.CSS_SELECTOR, "app-header-bottom li:nth-of-type(7) a")

    """ Buttons """

    @allure.step
    def open(self):
        self.open_page(MainPage.UNIQUE_LOCATOR)

    @allure.step
    def is_page_loaded(self):
        try:
            self.find(self.UNIQUE_LOCATOR)
            return True
        except TimeoutException:
            raise AssertionError(
                f"Not found unique locator: {self.UNIQUE_LOCATOR}")

    @allure.step
    def navigate_to_fedresurs(self):
        self.click(self.FEDRESURS_LINK)
        self.switch_to_last_window()

        from pages.fedresurs_page import FedresursPage
        return FedresursPage(self.browser)

    @allure.step
    def navigate_to_bidding(self):
        self.click(self.BIDDING_LINK)
        self.switch_to_last_window()

        from pages.fedresurs_page import SearchBiddingPage
        return SearchBiddingPage(self.browser)

    @allure.step
    def navigate_to_eaeu(self):
        self.click(self.EAEU_LINK)

        from pages.eaeu_page import EaeuPage
        return EaeuPage(self.browser)

    @allure.step
    def navigate_to_monitoring(self):
        self.click(self.MONITORING_LINK)
        self.switch_to_last_window()

        from pages.fedresurs_page import MonitoringPage
        return MonitoringPage(self.browser)

    @allure.step
    def navigate_to_news(self):
        self.click(self.NEWS_LINK)
        self.switch_to_last_window()

        from pages.fedresurs_page import NewsPage
        return NewsPage(self.browser)

    @allure.step
    def navigate_to_about_project(self):
        self.click(self.ABOUT_PROJECT_LINK)
        self.switch_to_last_window()

        from pages.fedresurs_page import AboutProjectPage
        return AboutProjectPage(self.browser)

    @allure.step
    def navigate_to_help(self):
        self.click(self.HELP_LINK)
        self.switch_to_last_window()

        from pages.fedresurs_page import HelpPage
        return HelpPage(self.browser)

    @allure.step
    def get_support_email(self):
        return self.get_text(self.SUPPORT_EMAIL)

    @allure.step
    def get_support_phones(self):
        return self.get_text(self.SUPPORT_PHONES)
