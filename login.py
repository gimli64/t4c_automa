from automa.api import *
from local_conf import PATH_TO_T4C

start(PATH_TO_T4C)

wait_until(Image(r"images\connect.jpg").exists, timeout_secs=10)
press(ENTER)

wait_until(Image(r"images\news.jpg").exists, timeout_secs=100)
press(ENTER)

wait_until(Image(r"images\enter_realms.jpg").exists, timeout_secs=10)
press(ENTER)

wait_until(Image(r"images\enter.jpg").exists, timeout_secs=10)
press(ENTER)
