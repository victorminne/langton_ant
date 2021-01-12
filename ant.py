import random
class Ants():

	direction = ["N","E","S","W"]
	color = ["white","black","blue","red","yellow","green","purple","pink","brown","cyan","indigo","orange"]

	def __init__(self, row, column, rules):
		self._live = True
		min_row, min_column = round(0.4*row), round(0.4*column)
		max_row, max_column = round(0.6*row), round(0.6*column)
		self._coordonate = [random.randint(min_row,max_row),random.randint(min_column,max_column)]
		self._orientation = 0
		self._current_direction = self.direction[self._orientation]
		self.rules = {}
		for i in range(len(rules)):
			self.rules[self.color[i]] = rules[i]

	def change_direction(self, color_of_the_case):

		orientaion_modificator = self.rules.get(color_of_the_case)
		if orientaion_modificator == "R":
			self._orientation += 1
		elif orientaion_modificator == "L":
			self._orientation -= 1
		elif orientaion_modificator == "B":
			self._orientation += 2


		self.update()

		index_color = self.color.index(color_of_the_case)+1
		if index_color == len(self.rules):
			index_color = 0

		return self.color[index_color]

	def bchange_direction(self, color_of_the_case):
		index_color = self.color.index(color_of_the_case)-1
		if index_color == -1:
			index_color = len(self.rules)-1

		orientaion_modificator = self.rules.get(self.color[index_color])
		if orientaion_modificator == "R":
			self._orientation -= 1
		elif orientaion_modificator == "L":
			self._orientation += 1
		elif orientaion_modificator == "B":
			self._orientation += 2

		self.update()

		return self.color[index_color]

	def update(self):
		if self._orientation < 0:
			self._orientation += 4
		elif self._orientation >3:
			self._orientation -= 4

		self._current_direction = self.direction[self._orientation]

	def set_coordonate(self, x, y):
		self._coordonate = [x, y]

	def direction_take(self):
		return self._current_direction

	def get_coordonate(self):
		return [self._coordonate[0],self._coordonate[1]]

	def alive(self):
		return self._live

	def dead(self, step):
		self._live = False
		self._step = step

	def resucite(self,step):
		if step == self._step:
			self._live = not self._live
			
		return self._live

	def __del__(self):
		print("bye")

class New_Ants():

	direction = ["N","E","S","W"]
	color = ["white","black","blue","red","yellow","green","purple","pink","brown","cyan","indigo","orange"]

	def __init__(self, row, column, rules, step):
		self._step = step
		self._live = True
		self._coordonate = [row,column]
		self._orientation = 0
		self._current_direction = self.direction[self._orientation]
		self.rules = {}
		for i in range(len(rules)):
			self.rules[self.color[i]] = rules[i]

	def change_direction(self, color_of_the_case):

		orientaion_modificator = self.rules.get(color_of_the_case)
		if orientaion_modificator == "R":
			self._orientation += 1
		elif orientaion_modificator == "L":
			self._orientation -= 1
		elif orientaion_modificator == "B":
			self._orientation += 2


		self.update()

		index_color = self.color.index(color_of_the_case)+1
		if index_color == len(self.rules):
			index_color = 0

		return self.color[index_color]

	def bchange_direction(self, color_of_the_case):
		index_color = self.color.index(color_of_the_case)-1
		if index_color == -1:
			index_color = len(self.rules)-1

		orientaion_modificator = self.rules.get(self.color[index_color])
		if orientaion_modificator == "R":
			self._orientation -= 1
		elif orientaion_modificator == "L":
			self._orientation += 1
		elif orientaion_modificator == "B":
			self._orientation += 2

		self.update()

		return self.color[index_color]

	def update(self):
		if self._orientation < 0:
			self._orientation += 4
		elif self._orientation >3:
			self._orientation -= 4

		self._current_direction = self.direction[self._orientation]

	def set_coordonate(self, x, y):
		self._coordonate = [x, y]

	def direction_take(self):
		return self._current_direction

	def get_coordonate(self):
		return [self._coordonate[0],self._coordonate[1]]

	def alive(self):
		return self._live

	def dead(self, step):
		self._live = False
		self._step = step

	def resucite(self,step):
		if step == self._step:
			self._live = not self._live
			
		return self._live

	def __del__(self):
		print("bye")