from pynput.keyboard import Key, Listener


# The key combination to check
COMBINATION_ALL = {Key.cmd, Key.ctrl, Key.alt, Key.left, Key.up, Key.right}
COMBINATION_LEFT = {Key.cmd, Key.ctrl, Key.alt, Key.left}
COMBINATION_MID = {Key.cmd, Key.ctrl, Key.alt, Key.up}
COMBINATION_RIGHT = {Key.cmd, Key.ctrl, Key.alt, Key.right}

# The currently active modifiers
key_set = set()


def key_task():
    def on_press(key):
        if key in COMBINATION_ALL:
            key_set.add(key)

            if all(k in key_set for k in COMBINATION_LEFT):
                print('All modifiers active!: left')
            elif all(k in key_set for k in COMBINATION_MID):
                print('All modifiers active!: mid')
            elif all(k in key_set for k in COMBINATION_RIGHT):
                print('All modifiers active!: right')

        if key == Key.esc:
            listener.stop()

    def on_release(key):
        try:
            key_set.remove(key)
        except KeyError:
            pass

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


