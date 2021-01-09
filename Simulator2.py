from tkinter import *
from Board import Board_steps
from tkinter.ttk import Labelframe
from tkinter import messagebox

class Simulator_steps():

	def __init__(self, indice, row, col, percentage, number_of_ant,border):
		self.label_one_var = StringVar()
		self.label_two_var = StringVar()
		self.col = col
		self._win_ant = Tk()
		self._steps = 0
		self.indice = indice
		self._win_ant.title(f"Langton's ant simulation {indice} steps {self._steps}")
		self._win_ant.geometry("1000x800")
		self._win_ant.resizable(False, True)
		self._screen_size = 800
		self._game = Board_steps(row, col, percentage, number_of_ant)
		self._board_real, self.coordonate_of_ants, self._steps = self._game.returnn()
		number_of_ant, number_of_cell = self._game.info()
		self.dimension = IntVar()
		self.dimension.set(value = 50)
		#The table stores the objects displayed on the screen
		self._board = [[0] * col for _ in range(0, row)]

		#The size of a cell in pixels
		self._px = self._screen_size // col
		self._py = self._screen_size // row
		#The canvas is created from the previous values
		self._frame_dimension = Labelframe(self._win_ant, text = "Simulation :", height = 60, width = 300)
		self._frame_dimension.grid(column = 0, columnspan=4, row = 0, rowspan=2, sticky = 'w')
		self._monCanvas = Canvas(self._frame_dimension, width=self._screen_size, height=self._screen_size, bg='ivory')
		self._monCanvas.pack()

		if border:
			for y in range(0, row):
				for x in range(0, col):
					self._board[y][x] = self._monCanvas.create_rectangle(x * self._px, y * self._py,
	                                                                     x * self._px + self._px, y * self._py + self._py,
	                                                                     fill='white', outline='black')
		else:
			for y in range(0, row):
				for x in range(0, col):
					self._board[y][x] = self._monCanvas.create_rectangle(x * self._px, y * self._py,
	                                                                     x * self._px + self._px, y * self._py + self._py,
	                                                                     fill='white', outline='white')

		self._board_real, self.coordonate_of_ants, self._steps = self._game.returnn()

		for i in range(len(self._board_real)):
			for j in range(len(self._board_real[0])):
				k = self._board_real[i][j]
				self._monCanvas.itemconfig(self._board[i][j], fill=k)

		for i in range(len(self.coordonate_of_ants)):
			self._monCanvas.itemconfig(self._board[self.coordonate_of_ants[i][0][0]][self.coordonate_of_ants[i][0][1]], fill='grey')

		self._frame_button = Labelframe(self._win_ant, text = "Steps settings :", height = 60, width = 300)
		self._frame_button.grid(column = 5, row = 0, sticky = 'w')
		self.scale_dimension = Scale(self._frame_button, orient = 'horizontal', from_ = 1, to = 1000, variable = self.dimension, tickinterval = 249, length = 175)
		self.scale_dimension.grid(column = 0, row = 0, padx = 5, pady = 5)
		self.button_simulator_steps = Button(self._frame_button, text = "Go forward", command = self.steps)
		self.button_simulator_steps.grid(column = 0 , row = 1, pady = 15)
		self.button_simulator_steps = Button(self._frame_button, text = "Go backward", command = self.bsteps)
		self.button_simulator_steps.grid(column = 0 , row = 2, pady = 15)
		self.button_simulator_steps = Button(self._frame_button, text = "Clear", command = self.clear)
		self.button_simulator_steps.grid(column = 0 , row = 3, pady = 15)
		self._monCanvas.bind("<ButtonPress-1>", self.mouseClick)
		self._frame_info = Labelframe(self._win_ant, text = "Info :", height = 60, width = 300)
		self._frame_info.grid(column = 5, row = 1, sticky = 'w')
		self.label_one = Label(self._frame_info, text = "Number of cell(s): " + str(number_of_cell))
		self.label_one.grid(column = 0, row = 0, sticky = 'w')
		self.label_two = Label(self._frame_info, text = "Number of cell(s): " + str(number_of_ant))
		self.label_two.grid(column = 0, row = 1, sticky = 'w')

		self._win_ant.mainloop()

	def steps(self):
		x = self.scale_dimension.get()
		self._game.play(x)
		self.actu()

	def bsteps(self):
		x = self.scale_dimension.get()
		self._game.bplay(x)
		self.actu()

	def actu(self):
		self._board_real, self.coordonate_of_ants, self._steps = self._game.returnn()

		for i in range(len(self._board_real)):
			for j in range(len(self._board_real[0])):
				k = self._board_real[i][j]
				self._monCanvas.itemconfig(self._board[i][j], fill=k)

		for i in range(len(self.coordonate_of_ants)):
			self._monCanvas.itemconfig(self._board[self.coordonate_of_ants[i][0][0]][self.coordonate_of_ants[i][0][1]], fill='grey')

		if self.coordonate_of_ants[0][1]:
			messagebox.showinfo("Info", "An ant want to go out, that's why the simulation cannot go either further or go back any further")


		self._win_ant.title(f"Langton's ant simulation {self.indice} steps {self._steps}")
		self.actu_info()

	def mouseClick(self,event):
		if self._game.maximum():

			tempo_x = -1
			tempo_y = -1
			for x in range(self.col):
				if (x*self._px)<event.x<=(x*self._px+self._px):
					tempo_y = x
					break

			for y in range(self.col):
				if (y*self._px)<event.y<=(y*self._px+self._px):
					tempo_x = y
					break

			if tempo_y != -1 and tempo_x != -1:
				self._game.create_new_ant(tempo_x,tempo_y)

			self._board_real, self.coordonate_of_ants, self._steps = self._game.returnn()

			for i in range(len(self._board_real)):
				for j in range(len(self._board_real[0])):
					k = self._board_real[i][j]
					self._monCanvas.itemconfig(self._board[i][j], fill=k)

			for i in range(len(self.coordonate_of_ants)):
				self._monCanvas.itemconfig(self._board[self.coordonate_of_ants[i][0][0]][self.coordonate_of_ants[i][0][1]], fill='grey')

		else:
			messagebox.showinfo("Info", "You can't add more ants")

		self.actu_info()

	def clear(self):
		self._game.clear()
		self._board_real, self.coordonate_of_ants, self._steps = self._game.returnn()

		for i in range(len(self._board_real)):
			for j in range(len(self._board_real[0])):
				k = self._board_real[i][j]
				self._monCanvas.itemconfig(self._board[i][j], fill=k)

		for i in range(len(self.coordonate_of_ants)):
			self._monCanvas.itemconfig(self._board[self.coordonate_of_ants[i][0][0]][self.coordonate_of_ants[i][0][1]], fill='grey')

		self.actu_info()

	def actu_info(self):
		number_of_ant, number_of_cell = self._game.info()
		self.label_one.config(text = "Number of cell(s): " + str(number_of_cell))
		self.label_two.config(text = "Number of ant(s): " + str(number_of_ant))