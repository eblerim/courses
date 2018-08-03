# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
	"""A rat caught in a maze."""

	# Write your Rat methods here.

	def __init__(self, symbol, row, col):
		"""(Rat, str, int, int) -> NoneType

		Precondition 1: len(symbol) == 1
		Precondition 2: row >= 0
		Precondition 3: col >= 0

		A Rat with symbol, row, col, and num_sprouts_eaten

		symbol: the 1-character symbol for the rat
		row: the row where the rat is located
		col: the column where the rate is located
		num_sprouts_eaten: the number of sprouts that this rat has eaten, which is initially 0.
		"""

		assert len(symbol) == 1, \
			'symbol is not 1-character.'
		assert row > 0, \
			'row must be equal or bigger than 0 since the row numbers start at 0, which is a wall.'
		assert col > 0, \
			'col must be equal or bigger than 0 since the col numbers start at 0, which is a wall.'
		
		self.symbol = symbol
		self.row = row
		self.col = col
		self.num_sprouts_eaten = 0

	def set_location(self, row, col):
		"""(Rat, int, int) -> NoneType

		Set the rat's row and col instance variables to the given row and column.
		"""

		assert row > 0, \
		   'row is not bigger than 0.'
		assert col > 0, \
		   'col is not bigger than 0.'

		self.row = row
		self.col = col

	def eat_sprout(self):
		"""(Rat) -> NoneType

		Add one to the rat's instance variable num_sprouts_eaten. Yuck.
		"""

		self.num_sprouts_eaten = self.num_sprouts_eaten + 1
		# self.num_sprouts_eaten += 1 # augmented assignment statement

	def __str__(self):
		"""(Rat) -> str

		Return a string representation of this Rat.
		"""

		return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)


class Maze:
	"""A 2D maze."""

	def __init__(self, maze, rat_1, rat_2):
		"""(Maze, list of list of str, Rat, Rat) -> NoneType

		Precondition 1: rows of the maze > 2
		Precondition 2: cols of the maze > 2
		Precondition 3: maze have the same number of columns in all rows
		Precondition 4: rat_1 inside maze and not on the wall and not on the sprout
		Precondition 5: rat_2 inside maze and not on the wall and not on the sprout

		Initialize a 2D maze with two rats and a number of uneaten sprouts.

		maze: the contents of the maze.
		rat_1: the first rat in the maze.
		rat_2: the second rat in the maze.
		num_sprouts_left: the number of uneaten sprouts in this maze.
		"""

		self.maze = maze
		self.rat_1 = rat_1
		self.rat_2 = rat_2

		self.maze[rat_1.row][rat_1.col] = rat_1.symbol
		self.maze[rat_2.row][rat_2.col] = rat_2.symbol

		num_sprouts_left = 0
		
		for row in maze:
			num_sprouts_left = num_sprouts_left + row.count(SPROUT)
		
		self.num_sprouts_left = num_sprouts_left

	def is_wall(self, row, col):
		"""(Maze, int, int) -> bool

		Precondition 1: 0 <= row < len(maze)
		Precondition 2: 0 <= col < len(maze[0])

		Return True if and only if there is a wall at the given row and column of the maze.
		"""

		assert 0 <= row < len(self.maze), \
			"Doesn't matches the number of rows of the maze."
		assert 0 <= col < len(self.maze[0]), \
			"Doesn't matches the number of columns of the maze."
		
		return self.get_character(row, col) == WALL

	def get_character(self, row, col):
		"""(Maze, int, int) -> str

		Precondition 1: 0 <= row < len(maze)
		Precondition 2: 0 <= col < len(maze[0])

		Return the character in the maze at the given row and column.
		If there is a rat at that location, then its character should
		be returned rather than HALL.
		"""

		assert 0 <= row < len(self.maze), \
		   "Doesn't matches the number of rows of the maze."

		assert 0 <= col < len(self.maze[0]), \
		   "Doesn't matches the number of columns of the maze."

		return self.maze[row][col]

	def move(self, rat, vertical, horizontal):
		"""(Maze, Rat, int, int) -> bool

		Precondition 1: vertical == UP or vertical == NO_CHANGE or vertical == DOWN
		Precondition 2: horizontal == LEFT or horizontal == NO_CHANGE or horizontal == RIGHT

		Move the rat in the given direction, unless there is a wall in the way.
		Also, check for a Brussels sprout at that location and, if present:
		- have the rat eat the Brussels sprout,
		- make that location a HALL, and
		- decrease the value that num_sprouts_left refers to by one.

		Return True if and only if there wasn't a wall in the way.
		"""

		assert vertical == UP or \
			   vertical == NO_CHANGE or \
			   vertical == DOWN, \
			   'Vertical direction wrong.'

		assert horizontal == LEFT or \
			   horizontal == NO_CHANGE or \
			   horizontal == RIGHT, \
			   'Horizontal direction wrong.'
	  
		new_row = rat.row + vertical
		new_col = rat.col + horizontal

		if self.is_wall(new_row, new_col):
			return False

		if self.get_character(new_row, new_col) == SPROUT:
			rat.eat_sprout()
			self.num_sprouts_left = self.num_sprouts_left - 1
			# self.num_sprouts_left -= 1 # augmented assignment statement
		self.maze[rat.row][rat.col] = HALL

		rat.set_location(new_row, new_col)

		self.maze[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol
		self.maze[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol

		return True

	def __str__(self):
		"""(Maze) -> str

		Return a string representation of this Maze.
		"""

		result = ''
		for row in self.maze:
			for char in row:
				result = result + char
			result = result + '\n'
		return result + "{0}\n{1}".format(self.rat_1, self.rat_2)
