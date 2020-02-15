# import threading
from queue import Queue

# from key_monitor import key_task
# from controller import control_task

from key_monitor import KeyTask
from controller import ControlTask



def main():
    threads = []
    q = Queue()

    # t1 = threading.Thread(target=key_task)
    # t1.daemon = True
    t1 = KeyTask(q)
    t1.start()
    threads.append(t1)

    # t2 = threading.Thread(target=control_task)
    # t2.daemon = True
    t2 = ControlTask(q)
    t2.start()
    threads.append(t2)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()

