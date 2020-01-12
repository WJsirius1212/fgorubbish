import PIL as pil
from PIL import ImageGrab

x1=85+385*2
y1=760
x2=x1+210
y2=y1+70


rect = (x1, y1, x2, y2)
#attack
rect2=(1615,910,1800,1000)
#start
rect3=(1665,1010,1905,1120)


img=ImageGrab.grab(rect3)
img.save('C:/Users/weijian/Desktop/start.png')


