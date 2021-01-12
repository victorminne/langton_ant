import threading
import time

from tkinter import *
from tkinter.ttk import Labelframe,OptionMenu
from tkinter import ttk
from tkinter import messagebox


from Board import Board_multiple_ants
from Simulator2 import Simulator_steps


class Parameters_wind(object):#Here y= row and x = column
	def __init__(self, master):
		self._rules = "RL"
		self._Game = []
		self._indice = 0
		frame = Frame(master)
		frame.grid()
		tabControl = ttk.Notebook(master)
		tabControl.configure(width= 420, height= 600)

		self.main_tab = ttk.Frame(tabControl)
		tabControl.add(self.main_tab, text= "Settings")
		tabControl.grid()

		self.about_tab = ttk.Frame(tabControl)
		tabControl.add(self.about_tab, text = "About")
		tabControl.grid()

		self.dimension = IntVar()
		self.dimension.set(value = 50)
		self.chkValue = BooleanVar() 
		self.chkValue.set(True)
		self.chkValue_two = BooleanVar() 
		self.chkValue_two.set(False)
		self.nbr_of_ant = IntVar()
		self.nbr_of_ant.set(value = 1)
		self.speed_opts = ['0','1000','500','250','100','50','10','0']
		self.speed = StringVar()
		self.black_case_nbr = IntVar()
		self.black_case_nbr.set(value = 0)
		
		self.about_page()
		self.main_page()

	def main_page(self):

		self.label_dimension = Label(self.main_tab, text = "How many row and column do you want ?")
		self.label_dimension.grid(column = 0, row = 0, sticky = 'w')
		self.scale_dimension = Scale(self.main_tab, orient = 'horizontal', from_ = 25, to = 200, variable = self.dimension, tickinterval = 25, length = 200)
		self.scale_dimension.grid(column = 0, row = 1, padx = 5, pady = 5)
		self.frame_dimension = Labelframe(self.main_tab, text = "Order of ideas :", height = 60, width = 300)
		self.frame_dimension.grid(column = 0, row = 2, sticky = 'w')
		dimension_frame_label = ["<50 this is a bit small","50<x<150 ideal dimension",">150 quite such huge"]
		for i in range(len(dimension_frame_label)):
			texte = dimension_frame_label[i]
			self.dimension_frame_label = Label(self.frame_dimension, text = f"{texte}")
			self.dimension_frame_label.grid(column = 0, row = i, sticky = 'w')
		self.dimension_frame_label.grid(column = 0, row = 2, sticky = 'w')
		self.label_ant = Label(self.main_tab, text = "How many ant(s) do you want ?")
		self.label_ant.grid(column = 0, row = 3, sticky = 'w')
		self.scale_ant = Scale(self.main_tab, orient = 'horizontal', from_ = 1, to = 10, variable = self.nbr_of_ant, tickinterval = 2, length = 200)
		self.scale_ant.grid(column = 0, row = 4, padx = 5, pady = 5)
		self.speed_label = Label(self.main_tab, text = "Delay in millisecond :")
		self.speed_label.grid(column = 0, row = 5, sticky = 'w')
		self.speed_menu = OptionMenu(self.main_tab, self.speed, *self.speed_opts)
		self.speed_menu.grid(column = 1, row = 5, sticky = 'w')
		self.black_case_label = Label(self.main_tab, text = "Percentage of black cells :")
		self.black_case_label.grid(column = 0, row = 6, sticky = 'w')
		self.black_case = Scale(self.main_tab, orient = 'horizontal', from_ = 0, to = 99, variable = self.black_case_nbr, tickinterval = 10, length = 200)
		self.black_case.grid(column = 0, row = 7, padx = 5, pady = 5)

		self.frame_rules = Labelframe(self.main_tab, text = "Rules setting:", height = 100, width = 400)
		self.frame_rules.grid(column = 0, row =8, sticky = 'w')
		self.label_rules = Label(self.frame_rules, text = "Rules :" + str(self._rules))
		self.label_rules.grid(column = 0, row = 0, sticky = 'w', columnspan = 3)
		self.button_F = Button(self.frame_rules, text = "F", command = self.F)
		self.button_F.grid(column = 1 , row = 1, padx = 5, pady = 5)
		self.button_L = Button(self.frame_rules, text = "L", command = self.L)
		self.button_L.grid(column = 0 , row = 2, padx = 5, pady = 5)
		self.button_clean = Button(self.frame_rules, text = "Clean", command = self.clean)
		self.button_clean.grid(column = 1 , row = 2, padx = 5, pady = 5)
		self.button_R = Button(self.frame_rules, text = "R", command = self.R)
		self.button_R.grid(column = 2 , row = 2, padx = 5, pady = 5)
		self.button_B = Button(self.frame_rules, text = "B", command = self.B)
		self.button_B.grid(column = 1 , row = 3, padx = 5, pady = 5)

		self.chk = Checkbutton(self.main_tab, text='Grid', var=self.chkValue) 
		self.chk.grid(column=0, row=9)
		self.chk_two = Checkbutton(self.main_tab, text='Desctructive collision', var=self.chkValue_two) 
		self.chk_two.grid(column=1, row=9)
		self.button_simulator = Button(self.main_tab, text = "Go to simulation auto", command = self.simulation_ants)
		self.button_simulator.grid(column = 0 , row = 10)
		self.button_simulator_steps = Button(self.main_tab, text = "Go to simulation step by step", command = self.simulation_steps)
		self.button_simulator_steps.grid(column = 1 , row = 10, pady = 15)


	def about_page(self):
		self.ligne = 0
		about_label = ["Students in the project :","      -Esteban Mathia","      -Victor Minne","      -Tom Cleenewerck"]
		for i in range(len(about_label)):
			texte = about_label[i]
			self.about_label = Label(self.about_tab, text = f"{texte}")
			self.about_label.grid(column = 0, row = self.ligne, sticky = 'w')
			self.ligne += 1

		esteban = ["Esteban :", "   +33675549372", "   esteban.mathia@supinfo.com"]
		victor = ["Victor :", "   +33611815452", "   victor.minne@supinfo.com"]
		tom = ["Tom :", "   +33750370032", "   tom.cleenewerck@supinfo.com"]
		info_contribuator = [esteban,victor,tom]
		for i in range(len(info_contribuator)):
			for j in range(len(info_contribuator[i])):
				texte = info_contribuator[i][j]
				self.about_label = Label(self.about_tab, text = f"{texte}")
				self.about_label.grid(column = 0, row = self.ligne, sticky = 'w')
				self.ligne += 1

	def F(self):
		if len(self._rules) < 12:
			self._rules += "F"
		else:
			messagebox.showinfo("Info", "You arrive to maximum rules")
		self.actu_rules()

	def L(self):
		if len(self._rules) < 12:
			self._rules += "L"
		else:
			messagebox.showinfo("Info", "You arrive to maximum rules")
		self.actu_rules()

	def R(self):
		if len(self._rules) < 12:
			self._rules += "R"
		else:
			messagebox.showinfo("Info", "You arrive to maximum rules")
		self.actu_rules()

	def B(self):
		if len(self._rules) < 12:
			self._rules += "B"
		else:
			messagebox.showinfo("Info", "You arrive to maximum rules")
		self.actu_rules()

	def clean(self):
		self._rules = ""
		self.actu_rules()

	def actu_rules(self):
		self.label_rules.config(text = "Rules :" + str(self._rules))

	def simulation_ants(self):
		threading._start_new_thread(self.new_board,())
		self._Game.append("")
		time.sleep(0.2)
		self._indice += 1

	def new_board(self):
		row = self.dimension.get()
		column = self.dimension.get()
		number_of_ant = self.nbr_of_ant.get()
		speed = int(self.speed.get())/1000
		percentage = self.black_case_nbr.get()
		border = self.chkValue.get()
		collision = self.chkValue_two.get()
		if len(self._rules) > 0:
			self._Game[self._indice] = Board_multiple_ants(collision, self._rules, border, self._indice, row, column, percentage, number_of_ant, speed)
		else:
			messagebox.showwarning("Warning", "The Rules are incorrect, please complete it")

	def simulation_steps(self):
		threading._start_new_thread(self.new_board_steps,())
		self._Game.append("")
		time.sleep(0.2)
		self._indice += 1

	def new_board_steps(self):
		row = self.dimension.get()
		column = self.dimension.get()
		number_of_ant = self.nbr_of_ant.get()
		percentage = self.black_case_nbr.get()
		border = self.chkValue.get()
		collision = self.chkValue_two.get()
		if len(self._rules) > 0:
			self._Game[self._indice] = Simulator_steps(collision, self._rules, self._indice, row, column, percentage, number_of_ant, border)
		else:
			messagebox.showwarning("Warning", "The Rules are incorrect, please complete it")