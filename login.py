from automa.api import *
from win32gui import GetWindowDC
from win32ui import *
from win32con import SRCCOPY

from local_conf import PATH_TO_T4C


window = start(PATH_TO_T4C)
width = window.width
height = window.height

windowDC = GetWindowDC(window.handle)
DC = CreateDCFromHandle(windowDC)
compatibleDC = DC.CreateCompatibleDC()	

dataBitMap = CreateBitmap()
dataBitMap.CreateCompatibleBitmap(DC, width, height)
compatibleDC.SelectObject(dataBitMap)
bmpfilenamename = "scrennshot.bmp"

def takeScreenshot():
	compatibleDC.BitBlt((0,0), (width, height) , DC, (0,0), SRCCOPY)
	dataBitMap.SaveBitmapFile(compatibleDC, bmpfilenamename)

wait_until(Image(r"images\connecter.jpg").exists, timeout_secs=10)
press(ENTER)

wait_until(Image(r"images\fleche.jpg").exists, timeout_secs=100)
press(ENTER)

wait_until(Image(r"images\jouer.jpg").exists, timeout_secs=10)
press(ENTER)

wait_until(Image(r"images\entrer.jpg").exists, timeout_secs=10)
press(ENTER)

takeScreenshot()
