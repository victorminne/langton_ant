from tkinter import *

class Simulation_wind():

	def __init__(self, row, col, border):
		self._win_ant = Tk()
		self._win_ant.title("Langton's ant")
		self._win_ant.geometry("800x800")
		self._win_ant.resizable(False, True)
		self._screen_size = 800

		#The table stores the objects displayed on the screen
		self._board = [[0] * col for _ in range(0, row)]

		#The size of a cell in pixels
		self._px = self._screen_size // col
		self._py = self._screen_size // row
		#The canvas is created from the previous values
		self._monCanvas = Canvas(self._win_ant, width=self._screen_size, height=self._screen_size, bg='ivory')
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

		self.refresh("Unkown", 0)

	def draw(self, y, x, color):
		self._monCanvas.itemconfig(self._board[y][x], fill=color)

	def refresh(self, indice, step):
		self._win_ant.title(f"Langton's ant. Simulation {indice}, step {step}")
		self._win_ant.update()

	def wait(self):
		self._win_ant.mainloop()
