from automa.api import *

connect = Image('connect.jpg')
news = Image('news.jpg')
enter_realms = Image('enter_realms.jpg')
enter = Image('enter.jpg')
compas = Image('compas.jpg')

start(r"C:\Program Files (x86)\The4ThComing\t4c.exe")

wait_until(connect.exists, timeout_secs=10)
press(ENTER)

wait_until(news.exists, timeout_secs=100)
press(ENTER)

wait_until(enter_realms.exists, timeout_secs=10)
press(ENTER)

wait_until(enter.exists, timeout_secs=10)
press(ENTER)
