import a2
import unittest


class TestRat(unittest.TestCase):
	"""Test class for class Rat."""

	def test_init_example_1(self):
		"""Test if the constructor is initialized correctly and we can access its instance variable(s)."""

		rat_1 = a2.Rat('P', 1, 4)
		self.assertEqual('P', rat_1.symbol)

	def test_init_example_2(self):
		"""Test if the constructor is initialized correctly and we can access its instance variable(s)."""
		
		rat_1 = a2.Rat('P', 1, 4)
		self.assertEqual(0, rat_1.num_sprouts_eaten)

	def test_set_location_row(self):
		"""Test if set_location_row method sets the rat's row instance variables to the given row."""
		
		rat_1 = a2.Rat('P', 1, 4)
		rat_1.set_location(3, 5)
		self.assertEqual(3, rat_1.row)

	def test_set_location_column(self):
		"""Test if set_location_column method sets the rat's column instance variables to the given column."""

		rat_1 = a2.Rat('P', 1, 4)
		rat_1.set_location(3, 5)
		self.assertEqual(5, rat_1.col)

	def test_eat_sprout(self):
		"""Test if eat_sprout method increases the value of num_sprouts_eaten instance variable as expected."""

		rat_1 = a2.Rat('P', 1, 4)
		rat_1.eat_sprout()
		self.assertEqual(1, rat_1.num_sprouts_eaten)

		
if __name__ == '__main__':
	unittest.main(exit=False)
