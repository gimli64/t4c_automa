from automa.api import *
from local_conf import PATH_TO_T4C

start(PATH_TO_T4C)

wait_until(Image(r"images\connecter.jpg").exists, timeout_secs=10)
press(ENTER)

wait_until(Image(r"images\fleche.jpg").exists, timeout_secs=100)
press(ENTER)

wait_until(Image(r"images\jouer.jpg").exists, timeout_secs=10)
press(ENTER)

wait_until(Image(r"images\entrer.jpg").exists, timeout_secs=10)
press(ENTER)
