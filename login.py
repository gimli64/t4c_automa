from automa.api import *

connect = Image('images\\connect.jpg')
news = Image('images\\news.jpg')
enter_realms = Image('images\\enter_realms.jpg')
enter = Image('images\\enter.jpg')
compas = Image('images\\compas.jpg')

start(r"C:\Program Files (x86)\The4ThComing\t4c.exe")

wait_until(connect.exists, timeout_secs=10)
press(ENTER)

wait_until(news.exists, timeout_secs=100)
press(ENTER)

wait_until(enter_realms.exists, timeout_secs=10)
press(ENTER)

wait_until(enter.exists, timeout_secs=10)
press(ENTER)
