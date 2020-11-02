from selenium.webdriver.common.by import By
from pomTests.homework5.locators import Locators

class SearchPage():
    def __init__(self, driver):
        self.driver = driver

        self.search_textbox_locators = Locators.search_textbox_locators
        self.search_button_locators = Locators.search_button_locators
        self.search_secondpage_locators = Locators.search_secondpage_locators
        self.secondpage_locators = Locators.secondpage_locators
        self.product_locators = Locators.product_locators

    def enter_search_text(self, text):
        self.driver.find_element(By.ID, self.search_textbox_locators).send_keys(text)
        assert (self.driver.find_element(By.ID, self.search_textbox_locators)).get_attribute("value") == text, "Az önce search ettiğin sayfada değilsin."

    def click_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_locators).click()

    def click_second_page(self):
        self.driver.find_element(By.XPATH, self.search_secondpage_locators).click()
        assert (self.driver.find_element(By.XPATH, self.secondpage_locators)).get_attribute("text") == "2", "İkinci sayfada değilsin."

    def click_product(self):
        self.driver.find_element(By.XPATH, self.product_locators).click()
