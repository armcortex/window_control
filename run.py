import threading

from key_monitor import key_task
from controller import control_task


def main():
    threads = []

    t1 = threading.Thread(target=key_task)
    t1.start()
    threads.append(t1)

    t2 = threading.Thread(target=control_task)
    t2.start()
    threads.append(t2)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()

