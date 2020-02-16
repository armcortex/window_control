from queue import Queue
from key_monitor import KeyTask
from controller import ControlTask


def main():
    threads = []
    q = Queue()

    t1 = KeyTask(q)
    t1.start()
    threads.append(t1)

    t2 = ControlTask(q)
    t2.start()
    threads.append(t2)

    # Start all threads
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()

