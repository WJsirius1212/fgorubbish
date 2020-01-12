import pic
import time
import win32gui
import PIL as pil
from PIL import ImageGrab
import win32api
import win32con
import time


time.sleep(4)

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def clickskillquick():

    print("skillquick!")

    win32api.SetCursorPos(pic.quick1)
    click()
    time.sleep(2)
    win32api.SetCursorPos(pic.him)
    click()
    time.sleep(5)
    time.sleep(1)


    win32api.SetCursorPos(pic.quick2)
    click()    
    time.sleep(2)
    win32api.SetCursorPos(pic.him)
    click()
    time.sleep(1)
    time.sleep(5)

def clickskillnp1():
    print("50np!")

    win32api.SetCursorPos(pic.np501)
    click()
    time.sleep(1)
    win32api.SetCursorPos(pic.him)
    click()
    time.sleep(1)
    time.sleep(5)


def clickskillnp2():
    print("50np!")


    win32api.SetCursorPos(pic.np502)
    click()
    time.sleep(1)
    win32api.SetCursorPos(pic.him)
    click()
    time.sleep(1)
    time.sleep(5)

def clickskilldown():
    print("down!")

    win32api.SetCursorPos(pic.down1)
    click()
    time.sleep(1)
    time.sleep(5)

    win32api.SetCursorPos(pic.down2)
    click()
    time.sleep(1)
    time.sleep(5)

def clickcard(First,Second):
    win32api.SetCursorPos(pic.canada)
    click()
    time.sleep(1)

    win32api.SetCursorPos(pic.card[First])
    click()
    time.sleep(1)

    win32api.SetCursorPos(pic.card[Second])
    click()
    time.sleep(1)

def twentynp():

    print("20np!")

    win32api.SetCursorPos(pic.master)
    click()
    time.sleep(1)
    win32api.SetCursorPos(pic.twentynp)
    click()
    time.sleep(1)
    win32api.SetCursorPos(pic.him)
    click()
    time.sleep(1)
    time.sleep(4)

def gold():
    print("golden!")

    win32api.SetCursorPos(pic.golden)
    click()
    time.sleep(1)
    time.sleep(5)

def clicknext():

    win32api.SetCursorPos(pic.next)
    click()
    time.sleep(0.5)


def attack():
    win32api.SetCursorPos(pic.att)
    click()
    time.sleep(2)


def clickatk():
    win32api.SetCursorPos(pic.atk)
    click()
    time.sleep(1)
    time.sleep(3)

def clickstars():
    win32api.SetCursorPos(pic.stars)
    click()
    time.sleep(1)
    time.sleep(3)

def merlin():

    print("20np!morestars!busterup!")
    time.sleep(2)
    win32api.SetCursorPos(pic.merlinone)
    click()
    time.sleep(5)

    win32api.SetCursorPos(pic.meilintwo)
    click()
    time.sleep(5)

    win32api.SetCursorPos(pic.meilinthree)
    click()
    time.sleep(0.5)
    win32api.SetCursorPos(pic.him)
    click()
    time.sleep(5)

    print("change merlin into cba!")
    win32api.SetCursorPos(pic.master)
    click()
    time.sleep(1)
    win32api.SetCursorPos(pic.changeman)
    click()
    time.sleep(1)
    win32api.SetCursorPos(pic.secondcba)
    click()
    win32api.SetCursorPos(pic.meilin)
    click()
    time.sleep(1)
    win32api.SetCursorPos(pic.yes)
    click()
    pic.times(9)

def clickopeninterface():
    win32api.SetCursorPos(pic.openinterface)
    click()
    time.sleep(2)

def clicksupport():
    win32api.SetCursorPos(pic.support)
    click()
    time.sleep(4)

# def wheeling(i):
#     place = (930, 200 + i * 27)
#     win32api.SetCursorPos(place)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#     i += 1
#     place = (930, 200 + i * 27)
#     win32api.SetCursorPos(place)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
#     time.sleep(0.5)

def f5():
    fresh=(625,120)
    win32api.SetCursorPos(fresh)
    click()
    time.sleep(1)
    yep = (625, 445)
    win32api.SetCursorPos(yep)
    click()
    time.sleep(4)

def startnow():
    win32api.SetCursorPos(pic.sta)
    click()
    time.sleep(10)

def clickmateratk():

    print("atk up!")
    win32api.SetCursorPos(pic.master)
    click()
    time.sleep(1)
    win32api.SetCursorPos(pic.masteratk)
    click()
    time.sleep(1)
    time.sleep(3)

def eatapple():
    plus=(120,540)
    win32api.SetCursorPos(plus)
    click()
    apple=(510,260)
    win32api.SetCursorPos(apple)
    click()
    time.sleep(1)
    yep = (630, 450)
    win32api.SetCursorPos(yep)
    click()
    time.sleep(4)