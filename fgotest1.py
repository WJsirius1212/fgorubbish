import win32gui
import PIL as pil
from PIL import ImageGrab
import win32api
import win32con
import time

#导入点击函数
import click
#导入选卡函数
import fgo_1 as choose
#导入识别函数
import check

def play(i):
    print('here we are in round_'.format(i+1))
    click.attack()
    First, Second = check.get_cards_and_play()
    click.clickcard(First, Second)
    time.sleep(60)



#卡组



'''
#开始
img=pic.start
scn=ImageGrab.grab(pic.star)

while(1):
    if img.getcolors()!=scn.getcolors():
        break
    win32api.SetCursorPos(pic.sta)
    click.click()
    sleep(1)


i=1
#stop
time.sleep(5)


#20np quick gold

'''
for i in range(3):
    if i==0:    
        #第一次判断
        click.twentynp()
        click.clickskillquick()
        click.gold()
    elif i==1:
        #第二次判断
        click.clickskillnp1()
    elif i==2:
        #第三次判断
        click.clickskilldown()
        click.clickskillnp2()
    
    play(i)
        
        
#结尾

click.clicknext()
        

