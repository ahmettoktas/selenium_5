from locators import search_page_locators, parameters
from base import BaseFunctions
import unittest


class SearchFunctions(BaseFunctions, unittest.TestCase):
    def search(self):
        self.input(search_page_locators.search_textbox, parameters.search_text)
        self.click(search_page_locators.search)
        self.assertTrue(self.wait_for_element(search_page_locators.search_textbox).get_attribute("value"), parameters.search_text)
        self.click(search_page_locators.second_page)

    def click_product(self):
        self.click(search_page_locators.product)
