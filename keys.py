#modules needed for proper working system
from pynput import keyboard
from pynput.keyboard import Controller
#combos, optimise
COMBINATIONS = [{keyboard.Key.alt,keyboard.KeyCode(char="n")},]
COMBINATIONS2 = [{keyboard.Key.alt, keyboard.KeyCode(char="N")}]
COMBINATIONS3 = [{keyboard.Key.alt,keyboard.KeyCode(char="c")},]
COMBINATIONS4 = [{keyboard.Key.alt, keyboard.KeyCode(char="C")}]
#some needed variables
keyboards = Controller()
current = set()
#ñ,Ñ,Ç,ç
def execute(char):
    keyboards.type(char)

#To do; optimise this crap, lots of bucle, possible if else statement for second key pressed when pressing alt+"{ç,ñ,Ñ,Ç}"?
def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute("ñ")
    elif any([key in COMBO for COMBO in COMBINATIONS2]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS2):
            execute("Ñ")
    elif any([key in COMBO for COMBO in COMBINATIONS3]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS3):
            execute("ç")
    elif any([key in COMBO for COMBO in COMBINATIONS4]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS4):
            execute("Ç")

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)
#detects keyboard pressing
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()