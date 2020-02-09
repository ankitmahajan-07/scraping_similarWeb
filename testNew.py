import pandas as pd
import webbrowser as wb
import time
import pyautogui

def keyBoardCopy():
    from pynput.keyboard import Key, Controller

    keyboard = Controller()

    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)

def keyBoardPaste():
    from pynput.keyboard import Key, Controller

    keyboard = Controller()

    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)

def altTab():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

abc = pd.read_excel('C:\\Users\\acer\\Downloads\\cds\\mat.xls', header=None, index_col=False)
# print(abc)

# print(abc)
# f = open('demo.txt', 'a')
# for item in abc.index:
#     print(abc[0][item])
#
#     f.write(abc[0][item] + ' --->>> ')
#     f.write('\n')

url = 'instagram.com'
wb.get().open_new_tab('https://instagram.com')

from pynput.mouse import Button, Controller

mouse = Controller()
mouse.position = (1230, 40)
time.sleep(5)
mouse.click(Button.left, 1)
mouse.position = (1170, 360)
time.sleep(5)
mouse.click(Button.left, 3)
time.sleep(1)
keyBoardCopy()
altTab()
# value = input('Enter value')
# keyBoardPaste()
# print(value)






