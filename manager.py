from automa.api import *
from win32gui import GetWindowDC
from win32ui import *
from win32con import SRCCOPY

class Manager:

	def __init__(self, window):
		self.window = window
		self.width = window.width
		self.height = window.height

		windowDC = GetWindowDC(window.handle)
		self.DC = CreateDCFromHandle(windowDC)
		self.compatibleDC = self.DC.CreateCompatibleDC()	

		self.dataBitMap = CreateBitmap()
		self.dataBitMap.CreateCompatibleBitmap(self.DC, self.width, self.height)
		self.compatibleDC.SelectObject(self.dataBitMap)

		self.bmpCounter = 0
		self.bmpFileName = "screenshot{0}.bmp".format(self.bmpCounter)

	def autoLogin(self):
		switch_to(self.window)
		wait_until(Image(r"images\connecter.jpg").exists, timeout_secs=10)
		press(ENTER)

		wait_until(Image(r"images\fleche.jpg").exists, timeout_secs=100)
		press(ENTER)

		wait_until(Image(r"images\jouer.jpg").exists, timeout_secs=10)
		press(ENTER)

		wait_until(Image(r"images\entrer.jpg").exists, timeout_secs=10)
		press(ENTER)


	def takeScreenshot(self):
		switch_to(self.window)
		self.compatibleDC.BitBlt((0,0), (self.width, self.height) , self.DC, (0,0), SRCCOPY)
		self.dataBitMap.SaveBitmapFile(self.compatibleDC, self.bmpFileName)

		self.bmpCounter += 1
		self.bmpFileName = "screenshot{0}.bmp".format(self.bmpCounter)
