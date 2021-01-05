import random
import time
from tkinter import messagebox
from Simulator import Simulation_wind
from Ant import Ants


class Board_multiple_ants():#here x = row and y = column

	color = ["blue","red","yellow","green","purple","pink","brown","cyan","indigo","orange"]

	def __init__(self, indice=int, row=int, column=int, percentage=int, number_of_ant=int, speed=0.1):
		self._step = 0
		self._indice = indice
		self._speed = speed
		self._test = True
		self._row = row
		self._column = column
		self._board = []
		#create a table with the colour of the square for each cell
		for _ in range(row):
			ligne =[]
			for _ in range(column):
				if random.randint(0,100) < percentage :
					ligne.append("black")
				else:
					ligne.append("white")

			self._board.append(ligne)

		#create a list of where to store each ant
		self._ants = []
		for _ in range(number_of_ant):
			self._ants.append("")

		for i in range(len(self._ants)):
			self._ants[i] = Ants(row, column, self.color[i])

		#initilisation of the window which display the langton's ant(s)
		self._window_of_game = Simulation_wind(row, column)
		#colorize each cells with the correct color
		for i in range(row):
			for j in range(column):
				k = self._board[i][j]
				self._window_of_game.draw(i, j, k)
		#Then colorize ant's cell with the correct color
		for i in self._ants:
			coordonate = i.get_coordonate()
			self._window_of_game.draw(coordonate[0], coordonate[1], "grey")

		self._window_of_game.refresh(self._indice, self._step)
		self.play()

	def finished(self):
		MsgBox = messagebox.askquestion ("Finish", f"The simulation {self._indice} finished, do want to let show ?",icon = 'warning')

		if MsgBox == 'yes':
			self._window_of_game.wait()
		else:
			print("goodbye my lover")

	def play(self):
		while self._test:
			for i in self._ants:
				self.move(i)
			time.sleep(self._speed)
			self._step += 1
			self._window_of_game.refresh(self._indice, self._step)
		self.finished()

	def move(self, current_ant):
		coordonate = current_ant.get_coordonate()
		color = current_ant.get_color()		
				
		if self._board[coordonate[0]][coordonate[1]] == "white":
			color_of_the_case = "white" 
		else:
			color_of_the_case = "not white"
		
		self._board[coordonate[0]][coordonate[1]] = current_ant.change_direction(color_of_the_case)
		self._window_of_game.draw(coordonate[0] , coordonate[1], self._board[coordonate[0]][coordonate[1]])
		
		x, y = self.direction_to_number(current_ant.direction_take())
		if self.condition(coordonate, x, y):
			return

		self._window_of_game.draw(coordonate[0] + x, coordonate[1] + y, 'grey')
		current_ant.set_coordonate(coordonate[0] + x, coordonate[1] + y)

	def direction_to_number(self, direction):
		if direction == "N":
			return -1, 0
		elif direction == "E":
			return 0, 1
		elif direction == "S":
			return 1, 0
		elif direction == "W":
			return 0, -1