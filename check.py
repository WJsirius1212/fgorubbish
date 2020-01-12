import PIL
import cv2
from PIL import ImageGrab
from PIL import Image
import names
import fgo_1 as choose
import time
import click
import win32api
import win32con
import pic

# 卡组判断
def get_cards_and_play():
    servant = []
    cards = []
    for i in range(5):
        for k in range(5):
            grab(i)
            for name in names.card_name:

                for color in names.card_color:
                    # img=Image.open(f"./Users/weijian/PycharmProjects/test/pic/{eval(name+color)}.png")
                    img = f"C:/Users/weijian/PycharmProjects/test/pic/{name + color}.png"
                    picture = f"C:/Users/weijian/PycharmProjects/test/pic/grab.png"
                    if check(picture, img):
                        servant.append(name)
                        cards.append(color)
                        break

            if len(servant) == i + 1: break;
            time.sleep(0.05)

        if len(servant) != i + 1:
            servant.append('err')
            cards.append('err')
    print("now,we know the card:")
    print(servant)
    print(cards)
    First, Second = choose.play_cards(servant, cards)
    print('we choose(0,1,2,3,4)\n', First, Second)
    return First, Second


# 截图
def grab(i):
    # 截图
    x1 = 85 + 385 * i
    y1 = 680
    x2 = x1 + 210
    y2 = y1 + 270
    rect = (x1, y1, x2, y2)
    img = ImageGrab.grab(rect)
    img.save('C:/Users/weijian/PycharmProjects/test/pic/grab.png')


def grabver_2():
    # 截图
    x1 = 0
    y1 = 0
    x2 = 500
    y2 = 500
    rect = (x1, y1, x2, y2)
    img = ImageGrab.grab(rect)
    img.save('C:/Users/weijian/PycharmProjects/test/pic/grab.png')


def grabver_3():
    # 截图
    x1 = 1250
    y1 = 510
    x2 = 1580
    y2 = 600
    rect = (x1, y1, x2, y2)
    img = ImageGrab.grab(rect)
    img.save('C:/Users/weijian/PycharmProjects/test/pic/grab.png')


# check
def check(picture, img):
    # picture.show()
    # img.show()
    template = cv2.imread(img)
    picture_change = cv2.imread(picture)

    res = cv2.matchTemplate(picture_change, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.7

    if (res >= threshold).any():
        return 1
    else:
        return 0


# 梦开始的地方
def checkopeninterface():
    # img = f"C:/Users/weijian/PycharmProjects/test/pic/openinterface.png"
    # picture = f"C:/Users/weijian/PycharmProjects/test/pic/grab.png"
    # while (check(picture, img) != 1):
    #     print("start to check.")
    #     time.sleep(0.1)
    #     grabver_2()
    #     picture = f"C:/Users/weijian/PycharmProjects/test/pic/grab.png"
    print("now ,we are in open-interface.")
    time.sleep(3)
    click.clickopeninterface()



def supportchoose():
    img = f"C:/Users/weijian/PycharmProjects/test/pic/skill.png"
    i = 0
    pic.times(3)
    while (1):
        grabver_3()
        picture = f"C:/Users/weijian/PycharmProjects/test/pic/grab.png"
        print("now we check：", i + 1)
        if check(picture, img):
            print("This is cba.")
            break
        else:
            print("check agian!")
            i += 1
            time.sleep(15)
            click.f5()

    time.sleep(3)
    click.clicksupport()

def checkend():
    # img = f"C:/Users/weijian/PycharmProjects/test/pic/endinterface.png"
    # picture = f"C:/Users/weijian/PycharmProjects/test/pic/grab.png"
    # while (check(picture, img) != 1):
    print("start end.")
    for i in range(20):

        click.clicknext()
        time.sleep(0.1)
        grabver_2()
        picture = f"C:/Users/weijian/PycharmProjects/test/pic/grab.png"
    print("now ,we are in end-interface.")


