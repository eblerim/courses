import a2
import unittest


class TestMaze(unittest.TestCase):
	"""Test class for class Maze."""

	def test_init_example1(self):
		"""Test if the constructor is initialized correctly and the rat(s) symbols(s) appear where they should."""

		maze_1 = a2.Maze([
						['#', '#', '#', '#', '#', '#', '#'],
						['#', '.', '.', '.', '.', '.', '#'],
						['#', '.', '#', '#', '#', '.', '#'],
						['#', '.', '.', '@', '#', '.', '#'],
						['#', '@', '#', '.', '@', '.', '#'],
						['#', '#', '#', '#', '#', '#', '#']
					   ],
						a2.Rat('J', 1, 1),
						a2.Rat('P', 1, 4))

		self.assertEqual([
						  ['#', '#', '#', '#', '#', '#', '#'],
						  ['#', 'J', '.', '.', 'P', '.', '#'],
						  ['#', '.', '#', '#', '#', '.', '#'],
						  ['#', '.', '.', '@', '#', '.', '#'],
						  ['#', '@', '#', '.', '@', '.', '#'],
						  ['#', '#', '#', '#', '#', '#', '#']
						 ], 
						  maze_1.maze)

	def test_init_example2(self):
		"""Test if the value of the instance variable num_sprouts_left is calculated correctly."""

		maze_1 = a2.Maze([
						['#', '#', '#', '#', '#', '#', '#'],
						['#', '.', '.', '.', '.', '.', '#'],
						['#', '.', '#', '#', '#', '.', '#'],
						['#', '.', '.', '@', '#', '.', '#'],
						['#', '@', '#', '.', '@', '.', '#'],
						['#', '#', '#', '#', '#', '#', '#']
					   ],
						a2.Rat('J', 1, 1),
						a2.Rat('P', 1, 4))

		self.assertEqual(3, maze_1.num_sprouts_left)

	def test_is_wall_true(self):
		"""Test if we can catch/calculate walls correctly at a give row and column of the maze."""

		maze_1 = a2.Maze([
						['#', '#', '#', '#', '#', '#', '#'],
						['#', '.', '.', '.', '.', '.', '#'],
						['#', '.', '#', '#', '#', '.', '#'],
						['#', '.', '.', '@', '#', '.', '#'],
						['#', '@', '#', '.', '@', '.', '#'],
						['#', '#', '#', '#', '#', '#', '#']
					   ],
						a2.Rat('J', 1, 1),
						a2.Rat('P', 1, 4))
		
		self.assertEqual(True, maze_1.is_wall(0, 0))

	def test_is_wall_false(self):
		"""Test if we can catch/calculate walls correctly at a give row and column of the maze."""

		maze_1 = a2.Maze([
						['#', '#', '#', '#', '#', '#', '#'],
						['#', '.', '.', '.', '.', '.', '#'],
						['#', '.', '#', '#', '#', '.', '#'],
						['#', '.', '.', '@', '#', '.', '#'],
						['#', '@', '#', '.', '@', '.', '#'],
						['#', '#', '#', '#', '#', '#', '#']
					   ],
						a2.Rat('J', 1, 1),
						a2.Rat('P', 1, 4))
		
		self.assertEqual(False, maze_1.is_wall(1, 2))

	def test_get_character_wall(self):
		"""Return the character in the maze at the given row and column, which in this case is # i.e. is a wall."""

		maze_1 = a2.Maze([
						['#', '#', '#', '#', '#', '#', '#'],
						['#', '.', '.', '.', '.', '.', '#'],
						['#', '.', '#', '#', '#', '.', '#'],
						['#', '.', '.', '@', '#', '.', '#'],
						['#', '@', '#', '.', '@', '.', '#'],
						['#', '#', '#', '#', '#', '#', '#']
					   ],
						a2.Rat('J', 1, 1),
						a2.Rat('P', 1, 4))
		
		self.assertEqual('#', maze_1.get_character(0, 0))

	def test_get_character_hallway(self):
		"""Return the character in the maze at the given row and column, which in this case is # i.e. is a hallway."""

		maze_1 = a2.Maze([
						['#', '#', '#', '#', '#', '#', '#'],
						['#', '.', '.', '.', '.', '.', '#'],
						['#', '.', '#', '#', '#', '.', '#'],
						['#', '.', '.', '@', '#', '.', '#'],
						['#', '@', '#', '.', '@', '.', '#'],
						['#', '#', '#', '#', '#', '#', '#']
					   ],
						a2.Rat('J', 1, 1),
						a2.Rat('P', 1, 4))
		
		self.assertEqual('.', maze_1.get_character(1, 2))

	def test_get_character_sprout(self):
		"""Return the character in the maze at the given row and column, which in this case is  @ i.e. is a Brussels sprout."""

		maze_1 = a2.Maze([
						['#', '#', '#', '#', '#', '#', '#'],
						['#', '.', '.', '.', '.', '.', '#'],
						['#', '.', '#', '#', '#', '.', '#'],
						['#', '.', '.', '@', '#', '.', '#'],
						['#', '@', '#', '.', '@', '.', '#'],
						['#', '#', '#', '#', '#', '#', '#']
					   ],
						a2.Rat('J', 1, 1),
						a2.Rat('P', 1, 4))
		
		self.assertEqual('@', maze_1.get_character(4, 1))

	def test_move_wall(self):
		"""Moving the rat in the direction where there is a wall."""

		no_change = 0
		up = -1
		rat_1 = a2.Rat('J', 1, 1)
		maze_1 = a2.Maze([
						['#', '#', '#', '#', '#', '#', '#'],
						['#', '.', '.', '.', '.', '.', '#'],
						['#', '.', '#', '#', '#', '.', '#'],
						['#', '.', '.', '@', '#', '.', '#'],
						['#', '@', '#', '.', '@', '.', '#'],
						['#', '#', '#', '#', '#', '#', '#']
					   ],
						a2.Rat('J', 1, 1),
						a2.Rat('P', 1, 4))

		self.assertEqual(False, maze_1.move(rat_1, up, no_change))

	def test_move_nowall(self):
		"""Moving the rat in the direction where there is not a wall but hall."""

		down = 1
		no_change = 0
		rat_1 = a2.Rat('J', 1, 1)
		maze_1 = a2.Maze([
						['#', '#', '#', '#', '#', '#', '#'],
						['#', '.', '.', '.', '.', '.', '#'],
						['#', '.', '#', '#', '#', '.', '#'],
						['#', '.', '.', '@', '#', '.', '#'],
						['#', '@', '#', '.', '@', '.', '#'],
						['#', '#', '#', '#', '#', '#', '#']
					   ],
						a2.Rat('J', 1, 1),
						a2.Rat('P', 1, 4))

		self.assertEqual(True, maze_1.move(rat_1, down, no_change))

	def test_move_eatensprouts(self):
		"""The number of eaten sprouts has increased after the rat has eaten one of them."""

		right = 1
		no_change = 0
		rat_1 = a2.Rat('J', 3, 2)
		maze_1 = a2.Maze([
						['#', '#', '#', '#', '#', '#', '#'],
						['#', '.', '.', '.', '.', '.', '#'],
						['#', '.', '#', '#', '#', '.', '#'],
						['#', '.', '.', '@', '#', '.', '#'],
						['#', '@', '#', '.', '@', '.', '#'],
						['#', '#', '#', '#', '#', '#', '#']
					   ],
						a2.Rat('J', 3, 2),
						a2.Rat('P', 1, 4))

		maze_1.move(rat_1, no_change, right)
		self.assertEqual(1, rat_1.num_sprouts_eaten)

	def test_move_leftsprouts(self):
		"""The number of sprouts in the maze has decreased after the rat has eaten one of them."""

		right = 1
		no_change = 0
		rat_1 = a2.Rat('J', 3, 2)
		maze_1 = a2.Maze([
						['#', '#', '#', '#', '#', '#', '#'],
						['#', '.', '.', '.', '.', '.', '#'],
						['#', '.', '#', '#', '#', '.', '#'],
						['#', '.', '.', '@', '#', '.', '#'],
						['#', '@', '#', '.', '@', '.', '#'],
						['#', '#', '#', '#', '#', '#', '#']
					   ],
						a2.Rat('J', 3, 2),
						a2.Rat('P', 1, 4))

		maze_1.move(rat_1, no_change, right)
		self.assertEqual(2, maze_1.num_sprouts_left)

	def test_move_makehall(self):
		"""Moving the rat in the direction where there is a wall."""

		right = 1
		no_change = 0
		up = -1
		down = 1
		rat_1 = a2.Rat('J', 3, 2)
		maze_1 = a2.Maze([
						['#', '#', '#', '#', '#', '#', '#'],
						['#', '.', '.', '.', '.', '.', '#'],
						['#', '.', '#', '#', '#', '.', '#'],
						['#', '.', '.', '@', '#', '.', '#'],
						['#', '@', '#', '.', '@', '.', '#'],
						['#', '#', '#', '#', '#', '#', '#']
					   ],
						a2.Rat('J', 3, 2),
						a2.Rat('P', 1, 4))
		
		maze_1.move(rat_1, no_change, right)
		maze_1.move(rat_1, down, no_change)
		
		self.assertEqual('.', maze_1.get_character(rat_1.row + up, rat_1.col + no_change))

if __name__ == '__main__':
	unittest.main(exit=False)
