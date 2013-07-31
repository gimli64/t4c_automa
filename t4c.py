from automa.api import start
from Tkinter import Tk, Button

from manager import Manager
from local_conf import PATH_TO_T4C


window = start(PATH_TO_T4C)
manager = Manager(window)

gui = Tk()

buttons = []
buttons.append(Button(gui, text = "Auto login", command = manager.autoLogin))
buttons.append(Button(gui, text = "Screenshot", command = manager.takeScreenshot))

for button in buttons:
	button.pack()

gui.mainloop()