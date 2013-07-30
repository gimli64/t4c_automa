from automa.api import *

start("C:\Program Files\The4ThComing\\t4c.exe")
wait_until(Image('C:\Users\Thomas\Desktop\images\connecter.jpg').exists)
press(ENTER)
wait_until(Image('C:\Users\Thomas\Desktop\images\\fleche.jpg').exists)
press(ENTER)
wait_until(Image('C:\Users\Thomas\Desktop\images\\jouer.jpg').exists)
press(ENTER)
press(ENTER)