import unittest

import product


class ProductTestCase(unittest.TestCase):
    def test_working(self) -> None:
        """
        Example of a passing test

        Details:
            - unittest would find zero tests if ProductTestCase had no methods
            - unittest also expects collections of one or more tests to be within unittest.TestCase objects
        """
        pass

    def test_transform_name_for_sku(self):
        """
        Illustrate using unittest.TestCase's custom assertions
        """
        small_black_shoes = product.Product("shoes", "S", "black")
        expected_value = "SHOES"
        actual_value = small_black_shoes.transform_name_for_sku()
        self.assertEqual(expected_value, actual_value)

    def test_transform_name_for_sku_fails(self):
        """
        Illustrate a failing test by tweaking expected value

        Details:
            - it is recommended to see your tests fail to confirm test is valid
        """
        small_black_shoes = product.Product("shoes", "S", "black")
        expected_value = "SHOEZ"
        actual_value = small_black_shoes.transform_name_for_sku()
        self.assertEqual(expected_value, actual_value)
