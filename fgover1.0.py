import win32gui
import PIL as pil
from PIL import ImageGrab
import win32api
import win32con
import time
import pic
import smtplib

# 导入点击函数
import click
# 导入选卡函数
import fgo_1 as choose
# 导入识别函数
import check


def play(i):
    print('here we are in round_',i+1)
    click.attack()
    First, Second = check.get_cards_and_play()
    click.clickcard(First, Second)
    pic.times(45)


x=eval(input("how much times do you want to play?\n"))

for m in range(x):
    print("TIMES:",m+1)

    # 开始
    pic.times(3)

    #open界面判断
    check.checkopeninterface()
    check.supportchoose()
    click.startnow()

    pic.times(25)

    for i in range(3):
        print("ROUND:",i+1)

        if i == 0:
            # 第一次判断
            click.merlin() #ver1.1
            click.clickskillquick()
            click.gold()
            pass
        elif i == 1:
            # 第二次判断
            click.clickskillnp1()
        elif i == 2:
            # 第三次判断
            click.clickstars()
            click.clickskilldown()
            click.clickskillnp2()
            click.clickatk()
            click.clickmateratk()

        play(i)

    # 结尾
    check.checkend()
    pic.times(30)

    if (m%7)==6:
        print("eat apple!")
        click.eatapple()
