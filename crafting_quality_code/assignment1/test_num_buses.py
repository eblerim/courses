import a1
import unittest


class TestNumBuses(unittest.TestCase):
	"""Test class for function a1.num_buses."""

	def test_num_buses_with_no_people(self):
		"""Test the number of buses required to transport 0 people i.e. no people."""

		actual = a1.num_buses(0)
		expected = 0
		self.assertEqual(expected, actual)

	def test_num_buses_with_2_people(self):
		"""Test the number of buses required to transport less than 50 and more than 0 people."""

		actual = a1.num_buses(2)
		expected = 1
		self.assertEqual(expected, actual)

	def test_num_buses_with_50_people(self):
		"""Test the number of buses required to transport just 50 people,
		which is a boundary/threshold case."""

		actual = a1.num_buses(50)
		expected = 1
		self.assertEqual(expected, actual)

	def test_num_buses_with_200_people(self):
		"""Test the number of buses required to transport 200 people,
		which is more than 50 and multiple of 50 people."""
		actual = a1.num_buses(200)
		expected = 4
		self.assertEqual(expected, actual)

	def test_num_buses_with_401_people(self):
		"""Test the number of buses required to transport 401 people,
		which is more than 50 and not multiple of 50 people."""

		actual = a1.num_buses(401)
		expected = 9
		self.assertEqual(expected, actual)


if __name__ == '__main__':
	unittest.main(exit=False)