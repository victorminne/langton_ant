from __future__ import unicode_literals
from tkinter import *
from tkinter import messagebox
from Parameters import Parameters_wind
import os

if __name__ == "__main__" :
	root = Tk()
	root.title("Langton's ant")
	root.resizable(False, False)
	os.chdir(os.path.dirname(os.path.realpath(__file__)))
	icon = PhotoImage(file='icon.png')
	root.iconphoto(False, icon)
	Parameters_wind(root)
	messagebox.showinfo("Info", "A simulation finish when an ant is out of border")
	root.mainloop()