from locators import parameters
from login import LoginFunctions
from search import SearchFunctions
from product import ProductFunctions
from base import BaseFunctions
from selenium import webdriver
import unittest


class TestRun(unittest.TestCase, BaseFunctions):

    def setUp(self):
        self.driver = webdriver.Chrome(parameters.driver_path)
        self.driver.maximize_window()
        self.driver.get(parameters.website_link)
        self.login_functions = LoginFunctions(driver=self.driver)
        self.product_functions = ProductFunctions(driver=self.driver)
        self.search_functions = SearchFunctions(driver=self.driver)

    def test(self):
        self.login_functions.navigate_to_login()
        self.login_functions.login()
        self.search_functions.search()
        self.search_functions.click_product()
        self.product_functions.add_to_wishlist()
        self.product_functions.navigate_to_wishlist_page()
        self.product_functions.delete_product()

    def TearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
