import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_k_empty_list(self):
        """Test swap_k with an empty list."""

        L = []
        a1.swap_k(L, 0)
        expected = []
        self.assertEqual(L, expected)

    def test_swap_k_one_element_list_and_k0(self):
        """Test swap_k with one element list, i.e. a singleton list, and k=0."""

        L = [1]
        a1.swap_k(L, 0)
        expected = [1]
        self.assertEqual(L, expected)

    def test_swap_k_two_element_list_and_k0(self):
        """Test swap_k with two element list and k=0."""

        L = [1, 2]
        a1.swap_k(L, 0)
        expected = [1, 2]
        self.assertEqual(L, expected)

    def test_swap_k_two_element_list_and_k1(self):
        """Test swap_k with one element list, i.e. a singleton list, and k=1."""

        L = [1, 2]
        a1.swap_k(L, 1)
        expected = [2, 1]
        self.assertEqual(L, expected)

    def test_swap_k_odd_element_list_and_kmax(self):
        """Test swap_k with an odd length list and k=len(L)//2."""

        L = [1, 2, 3, 4, 5]
        a1.swap_k(L, 2)
        expected = [4, 5, 3, 1, 2]
        self.assertEqual(L, expected)

    def test_swap_k_even_element_list_and_kmax(self):
        """Test swap_k with an even length list and k=len(L)//2."""

        L = [1, 2, 3, 4, 5, 6]
        a1.swap_k(L, 3)
        expected = [4, 5, 6, 1, 2, 3]
        self.assertEqual(L, expected)


if __name__ == '__main__':
    unittest.main(exit=False)