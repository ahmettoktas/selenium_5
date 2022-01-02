from homework5.locators import product_page_locators
from homework5.base import BaseFunctions
import unittest


class ProductFunctions(BaseFunctions, unittest.TestCase):
    def add_to_wishlist(self):
        self.click(product_page_locators.add_to_wishlist)

    def navigate_to_wishlist_page(self):
        product_text = self.wait_for_element(product_page_locators.product_text).text
        self.click(product_page_locators.wishlist)
        self.assertTrue(product_text, self.wait_for_element(product_page_locators.in_wishlist_product_text).text)

    def delete_product(self):
        product_text = self.wait_for_element(product_page_locators.in_wishlist_product_text).text
        self.click(product_page_locators.delete)
        self.assertFalse(product_text, self.wait_for_element(product_page_locators.in_wishlist_product_text).text)
