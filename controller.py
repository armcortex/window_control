import threading
import subprocess
import time
from screeninfo import get_monitors

cmd_focus = 'xdotool getwindowfocus'
cmd_move = 'xdotool windowmove {} {} {}'
cmd_resize = 'xdotool windowsize {} {} {}'

class ControlTask(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.daemon = True

    def run_cmd(self, cmd):
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, err = proc.communicate()
        time.sleep(0.01)
        return out.decode().strip()

    def run(self):
        # Get monitor information
        height, width = 0, 0
        for m in get_monitors():
            if m.name == 'DP-1':
                height, width = m.height, m.width
        if height == 0 and width == 0:
            raise ValueError('Cannot find right monitor')

        # Control window
        while True:
            dir_cmd = self.queue.get()
            if dir_cmd is None:
                return
            else:
                offset_x = 65       # tool bar size

                # Get window id
                focus = self.run_cmd(cmd_focus)

                # move and resize
                pos_x, pos_y = 0, 0
                size_x, size_y = 0, height
                if dir_cmd == 'LEFT':
                    pos_x = 0
                    size_x = int(width / 4) - offset_x
                elif dir_cmd == 'MID':
                    pos_x = int(width / 4)
                    size_x = int(width / 2)
                elif dir_cmd == 'RIGHT':
                    pos_x = int(width * 3 / 4)
                    size_x = int(width / 4)
                else:
                    raise ValueError('Command not support: {}'.format(dir_cmd))

                # must run resize command first then move command
                self.run_cmd(cmd_resize.format(focus, size_x, size_y))
                self.run_cmd(cmd_move.format(focus, pos_x, pos_y))
                # self.run_cmd(cmd_move.format(focus, pos_x, pos_y))
                # self.run_cmd(cmd_resize.format(focus, size_x, size_y))

                print('Pos x: {} y: {}, Size x: {} y: {}'.format(pos_x, pos_y, size_x, size_y))
