from pystray import Icon, Menu, MenuItem
from PIL import Image
from threading import Thread
import keyboard
import pyautogui


press_key = False
active = False


def press(event):
    global press_key
    press_key = not press_key


keyboard.on_press(press)


def toggle_case_change():
    global active
    active = not active
    Thread(target=case_changer).start()


def stop():
    global active
    active = False
    icon.stop()


def case_changer():
    while active:
        if press_key:
            pyautogui.press("capslock")


icon_image = Image.open("icon.ico")

icon = Icon("Sticky Caps", icon_image,  title="Sticky Caps", menu=Menu(
    MenuItem("Enable", toggle_case_change, lambda x: active),
    MenuItem("Exit", stop),
))

icon.run()
