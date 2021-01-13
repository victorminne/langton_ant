import random
import time
from tkinter import messagebox
from Simulator import Simulation_wind
from Ant import Ants,New_Ants


class Board_multiple_ants():#here x = row and y = column

	color = ["blue","red","yellow","green","purple","pink","brown","cyan","indigo","orange"]

	def __init__(self, collision, rules, border, indice=int, row=int, column=int, percentage=int, number_of_ant=int, speed=0.1):
		self._collision = collision
		self.rules = rules
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
			self._ants[i] = Ants(row, column, self.rules)

		#initilisation of the window which display the langton's ant(s)
		self._window_of_game = Simulation_wind(row, column, border)
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
				if i.alive():
					self.move(i)
				else:
					if i.resucite(self._step+1):
						self.move(i)

			if self._collision:
				self.collisionf()
				self.actu_ant()
				if not self.one_alive():
					break
			time.sleep(self._speed)
			self._step += 1
			self._window_of_game.refresh(self._indice, self._step)
		self.finished()

	def one_alive(self):
		count = 0
		for i in self._ants:
			if i.alive():
				count += 1

		if count == 0:
			return False
		else:
			return True

	def actu_ant(self):
		for i in self._ants:
			if not i.alive():
				coo = i.get_coordonate()
				self._window_of_game.draw(coo[0] , coo[1], self._board[coo[0]][coo[1]])

	def collisionf(self):
		if len(self._ants)>1:
			for i in range(len(self._ants)):
				if not self._ants[i].alive():
					continue
				coo_ant_one = self._ants[i].get_coordonate()
				for j in range(1,len(self._ants)-i):
					if self._ants[-j].alive():
						if coo_ant_one == self._ants[-j].get_coordonate():
							self._ants[i].dead(self._step)
							self._ants[-j].dead(self._step)
							break

	def move(self, current_ant):
		coordonate = current_ant.get_coordonate()

		self._board[coordonate[0]][coordonate[1]] = current_ant.change_direction(self._board[coordonate[0]][coordonate[1]])
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
			
	def condition(self,coordonate=list, x=int, y=int):
		if coordonate[0] + x >= self._row or coordonate[1] + y >= self._column:
			self._test = False
			return True
		elif coordonate[0] + x < 0 or coordonate[1] + y < 0:
			self._test = False
			return True

	def __del__(self):
		print("bye")


class Board_steps():#here x = row and y = column

	def __init__(self,collision, rules, row=int, column=int, percentage=int, number_of_ant=int):
		self._collision = collision
		self.rules = rules
		self._percentage = percentage
		self._number_of_ant = number_of_ant
		self._step = 0
		self._testt = False
		self._testta = False
		self._testtb = False
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
			self._ants[i] = Ants(row, column, self.rules)

	def returnn(self):
		coordonate_ants = []
		for i in self._ants:
			if not i.alive():
				ants = []
				ants.append([-1,-1])
				ants.append([self._testta,self._testtb])
				coordonate_ants.append(ants)
			else:
				ants = []
				ants.append(i.get_coordonate())
				ants.append([self._testta,self._testtb])
				coordonate_ants.append(ants)

		return self._board, coordonate_ants, self._step


	def play(self,steps):
		for i in range(steps):
			if self._testta == False:
				self._testtb = False
				for i in self._ants:
					if i.alive():
						if self.move(i):
							self._testta = True
					else:
						if i.resucite(self._step+1):
							if self.move(i):
								self._testta = True

				if self._collision:
					self.collisionf()

				self._step += 1

	def bplay(self,steps):
		for i in range(steps):
			if self._testtb == False:
				self._testta = False
				for i in self._ants[::-1]:
					if i.alive():
						if self.bmove(i):
							self._testtb = True
					else:
						if i.resucite(self._step-1):
							if self.bmove(i):
								self._testtb = True

				if self._collision:
					self.collisionf()

				self._step -= 1

	def collisionf(self):
		if len(self._ants)>1:
			for i in range(len(self._ants)):
				if not self._ants[i].alive():
					continue
				coo_ant_one = self._ants[i].get_coordonate()
				for j in range(1,len(self._ants)-i):
					if self._ants[-j].alive():
						if coo_ant_one == self._ants[-j].get_coordonate():
							self._ants[i].dead(self._step)
							self._ants[-j].dead(self._step)
							break

	def move(self, current_ant):
		coordonate = current_ant.get_coordonate()

		self._board[coordonate[0]][coordonate[1]] = current_ant.change_direction(self._board[coordonate[0]][coordonate[1]])
		
		x, y = self.direction_to_number(current_ant.direction_take())
		if self.condition(coordonate, x, y):
			self._board[coordonate[0]][coordonate[1]] = current_ant.bchange_direction(self._board[coordonate[0]][coordonate[1]])
			return True

		current_ant.set_coordonate(coordonate[0] + x, coordonate[1] + y)
		return False

	def bmove(self, current_ant):
		coordonate = current_ant.get_coordonate()

		x, y = self.bdirection_to_number(current_ant.direction_take())
		if self.condition(coordonate, x, y):
			return True

		self._board[coordonate[0]+x][coordonate[1]+y] = current_ant.bchange_direction(self._board[coordonate[0]+x][coordonate[1]+y])
		current_ant.set_coordonate(coordonate[0] + x, coordonate[1] + y)
		return False

	def direction_to_number(self, direction):
		if direction == "N":
			return -1, 0
		elif direction == "E":
			return 0, 1
		elif direction == "S":
			return 1, 0
		elif direction == "W":
			return 0, -1

	def bdirection_to_number(self, direction):
		if direction == "N":
			return 1, 0
		elif direction == "E":
			return 0, -1
		elif direction == "S":
			return -1, 0
		elif direction == "W":
			return 0, 1
			
	def condition(self,coordonate=list, x=int, y=int):
		if coordonate[0] + x >= self._row or coordonate[1] + y >= self._column:
			self._test = False
			return True
		elif coordonate[0] + x < 0 or coordonate[1] + y < 0:
			self._test = False
			return True

	def create_new_ant(self, row, column):
		self._ants.append("")
		self._ants[-1] = New_Ants(row, column, self.rules, self._step)

	def clear(self):
		self._step = 0
		self._testt = False
		self._test = True
		self._board = []
		for _ in range(self._row):
			ligne =[]
			for _ in range(self._column):
				if random.randint(0,100) < self._percentage :
					ligne.append("black")
				else:
					ligne.append("white")

			self._board.append(ligne)

		self._ants = []
		for _ in range(self._number_of_ant):
			self._ants.append("")

		for i in range(len(self._ants)):
			self._ants[i] = Ants(self._row, self._column, self.rules)

	def info(self):
		count = 0
		for i in self._ants:
			if i.alive():
				count += 1
		number_of_ant = [len(self._ants)-count,count]
		total = 0
		for i in range(len(self._board)):
			total += self._board[i].count("white")
		number_of_cell = self._column**2 - total
		return number_of_ant, number_of_cell

	def __del__(self):
		print("bye")