import unittest

import shopping_cart
import product


def get_one_product():
    """
    generate and return one default product

        note: due to an initial misunderstanding stemming from using this
        to de-duplicate, this is not an ideal unit testing framework and
        is probably too tightly coupled. As this is for practice/education,
        this is good enough for now.
    """
    product_ = product.Product("shoes", "S", "black")
    return product_


def one_item_cart():
    """
    Create a shopping cart and add one item to it
    """
    cart = shopping_cart.ShoppingCart()
    product_ = get_one_product()
    cart.add_product(product=product_)
    return cart


class CartTestCases(unittest.TestCase):
    def test_add_product(self) -> None:
        """
        When we add one product there should be one product in cart
        """
        cart = one_item_cart()
        expected_value = {"SHOES-S-BLACK": {"quantity": 1}}
        actual_value = cart.products
        self.assertDictEqual(expected_value, actual_value)

    def test_remove_product(self) -> None:
        """
        When we add one product and remove one product there should be zero products
        """
        cart = one_item_cart()
        product_ = get_one_product()
        cart.remove_product(product=product_, quantity=1)
        expected_value = {}
        actual_value = cart.products
        self.assertDictEqual(expected_value, actual_value)

    def test_product_remove_two(self) -> None:
        """
        When we add one product to cart and try to remove two, cart shouldn't be negative

            Hillard heavily hints his implementation has a bug like this
            It may be slightly different than I first assumed, however
        """
        cart = one_item_cart()
        product_ = get_one_product()
        cart.remove_product(product=product_, quantity=2)
        expected_value = {}
        actual_value = cart.products
        self.assertDictEqual(expected_value, actual_value)
