import product


def make_test_sku():
    """
    Create a sample SKU based on the docstring example
    """
    p = product.Product(name="shoes", size="S", color="black")
    return p


class TestProduct():
    def test_name_case(self) -> None:
        """
        Test method transform_name_for_sku returns upper case
        """
        p = make_test_sku()
        expected_value = "SHOES"
        actual_value: str = p.transform_name_for_sku()
        assert expected_value == actual_value

    def test_color_case(self) -> None:
        """
        Test method transform_color_for_sku return upper case
        """
        p = make_test_sku()
        expected_value = "BLACK"
        actual_value = p.transform_color_for_sku()
        assert expected_value == actual_value

    def test_generate_sku(self):
        """
        Test method transform_name_for_sku
        """
        p = make_test_sku()
        expected_value = "SHOES-S-BLACK"
        actual_value = p.generate_sku()
        assert expected_value == actual_value
