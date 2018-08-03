import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stock_price_summary_with_empty_list(self):
        """Test stock_price_summary with an empty list ."""

        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_with_one_pos_element(self):
        """Test stock_price_summary with one positive element."""

        actual = a1.stock_price_summary([0.01])
        expected = (0.01, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_with_one_neg_element(self):
        """Test stock_price_summary with one negative element."""

        actual = a1.stock_price_summary([-0.01])
        expected = (0, -0.01)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_with_one_pos_and_one_neg_element(self):
        """Test stock_price_summary with one negative element."""

        actual = a1.stock_price_summary([0.01, -0.01])
        expected = (0.01, -0.01)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_with_only_pos_elements(self):
        """Test stock_price_summary with only positive elements."""

        actual = a1.stock_price_summary([0.01, 0.02, 0.03])
        expected = (0.06, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_with_only_neg_elements(self):
        """Test stock_price_summary with only negative elements."""

        actual = a1.stock_price_summary([-0.01, -0.02, -0.03])
        expected = (0, -0.06)
        self.assertEqual(actual, expected)


    def test_stock_price_summary_general_case(self):
        """
        Test stock_price_summary where the items appear 
        in a random (mixed) way, which is a more general case. 
        """

        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)