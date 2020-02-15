import threading
import subprocess
import copy
import time
from screeninfo import get_monitors

cmd = ['xdotool getwindowfocus getwindowname']


# def control_task():
class ControlTask(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.daemon = True

    def run(self):
        # Get monitor information
        height, width = 0, 0
        for m in get_monitors():
            if m.name == 'DP-1':
                height, width = m.height, m.width
        if height == 0 and width == 0:
            raise ValueError('Cannot find right monitor')

        # Find focus windows
        while True:
            dir_cmd = self.queue.get()
            if dir_cmd is None:
                return
            else:
                print('Dir: {}'.format(dir_cmd))

                proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
                out, err = proc.communicate()
                name = copy.deepcopy(out).decode().strip().split(' - ')[-1]
                print('Program: {}, Title: {}'.format(name, out.decode(encoding='UTF-8').strip()))

