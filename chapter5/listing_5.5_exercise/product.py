# exercise is to test this code, hence the duplication


class Product:
    def __init__(self, name, size, color):
        self.name: str = name
        self.size: str = size
        self.color: str = color

    def transform_name_for_sku(self) -> str:
        return self.name.upper()

    def transform_color_for_sku(self) -> str:
        return self.color.upper()

    def generate_sku(self) -> str:
        """
        Generates a SKU for this product.

        Example:
            >>> small_black_shoes = Product('shoes', 'S', 'black')
            >>> small_black_shoes.generate_sku()
            'SHOES-S-BLACK'
        """
        name: str = self.transform_name_for_sku()
        color: str = self.transform_color_for_sku()
        return f"{name}-{self.size}-{color}"
