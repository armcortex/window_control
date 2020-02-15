import os
import time

cmd = 'xdotool getwindowfocus getwindowname'


def control_task():
    while True:
        result = os.system(cmd)
        # print('Result: {}'.format(result))
        time.sleep(1)
