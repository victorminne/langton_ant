import random
class Ants():

	direction = ["N","E","S","W"]

	def __init__(self, row, column, color):
		min_row, min_column = round(0.4*row), round(0.4*column)
		max_row, max_column = round(0.6*row), round(0.6*column)
		self._coordonate = [random.randint(min_row,max_row),random.randint(min_column,max_column)]
		self._orientation = 0
		self._current_direction = self.direction[self._orientation]
		self._color = color

	def change_direction(self, color_of_the_case):
		#white go to the rigth but not white go to the left
		self._orientation += 1 if color_of_the_case == "white" else -1 #if it's white then +1 else -1

		if self._orientation < 0:
			self._orientation += 4
		elif self._orientation >3:
			self._orientation -= 4

		self._current_direction = self.direction[self._orientation]

		if color_of_the_case == "white":
			return self._color
		else :
			return 'white'
