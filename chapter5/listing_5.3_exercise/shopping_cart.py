# exercise is to test this code

from collections import defaultdict

class ShoppingCart:
    def __init__(self):
        self.products = defaultdict(lambda: defaultdict(int))

    def add_product(self, product: str, quantity: int=1):
        self.products[product.generate_sku()]['quantity'] += quantity

    def remove_product(self, product: str, quantity: int=1):
        sku = product.generate_sku()
        self.products[sku]['quantity'] -= quantity
        if self.products[sku]['quantity'] == 0:
            del self.products[sku]
