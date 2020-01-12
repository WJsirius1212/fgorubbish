
#虽然我代码质量差啊但是我写得快啊，有空再改8
# 
# from PIL import Image
# from PIL import ImageGrab
# import fgo_1 as choose
import time
import smtplib
import email.header
import email.mime.text
# # 
# start=Image.open('C:/Users/weijian/PycharmProjects/test/pic/start.png')
# attack=Image.open('C:/Users/weijian/PycharmProjects/test/pic/attack.png')
# cbaa=Image.open('C:/Users/weijian/PycharmProjects/test/pic/cbaa.png')
# cbab=Image.open('C:/Users/weijian/PycharmProjects/test/pic/cbab.png')
# cbaq=Image.open('C:/Users/weijian/PycharmProjects/test/pic/cbaq.png')
# cbasa=Image.open('C:/Users/weijian/PycharmProjects/test/pic/cbasa.png')
# cbasb=Image.open('C:/Users/weijian/PycharmProjects/test/pic/cbasb.png')
# cbasq=Image.open('C:/Users/weijian/PycharmProjects/test/pic/cbasb.png')
# manb=Image.open('C:/Users/weijian/PycharmProjects/test/pic/manb.png')
# mana=Image.open('C:/Users/weijian/PycharmProjects/test/pic/mana.png')
# manq=Image.open('C:/Users/weijian/PycharmProjects/test/pic/manq.png')


#where to click
sta=(900,530)
att=(850,450)
golden=(600,450)
quick2=(295,450)
quick1=(55,450)
master=(895,255)

changeman=(800,250)
twentynp=(745,250)
masteratk=(690,250)

merlinone=(280,450)
meilintwo=(360,450)
meilinthree=(440,450)

next=(805,530)

secondcba=(550,280)
meilin=(260,280)
yes=(500,500)

him=(720,350)
down1=(120,450)
down2=(360,450)
np501=(190,450)
np502=(430,450)
card=[(100,400),(300,400),(500,400),(700,400),(900,400)]
canada=(660,180)
#where to screenshot
star=(1665,1010,1905,1120)
atta=(1615,910,1800,1000)


atk=(295+240,450)
stars=(430+240,450)


openinterface=(700,150)
support=(500,250)

# 
# def dis():
#     servant=[]
#     cards=[]
#     #截图坐标
#     picture=[]
#     #截图
#     for i in range(5):
#         x1 = 85 + 385 * i
#         y1 = 760
#         x2 = x1 + 210
#         y2 = y1 + 70
#         rect = (x1, y1, x2, y2)
#         img=ImageGrab.grab(rect)
#         picture.append(img)
#     #判断
#     cbaac=cbaa.getcolors(pic.cbaa.size[0]*pic.cbaa.size[1])
#     cbabc=cbab.getcolors(pic.cbab.size[0]*pic.cbab.size[1])
#     cbaqc=cbaq.getcolors(pic.cbaq.size[0]*pic.cbaq.size[1])
#     cbasac=cbasa.getcolors(pic.cbasa.size[0]*pic.cbasa.size[1])
#     cbasbc=cbasb.getcolors(pic.cbasb.size[0]*pic.cbasb.size[1])
#     cbasqc=cbasq.getcolors(pic.cbasq.size[0]*pic.cbasq.size[1])
#     cbaac = cbaa.getcolors(pic.cbaa.size[0] * pic.cbaa.size[1])
#     cbaac=cbaa.getcolors(pic.cbaa.size[0]*pic.cbaa.size[1])
#     cbaac = cbaa.getcolors(pic.cbaa.size[0] * pic.cbaa.size[1])
#     manac=mana.getcolors(pic.mana.size[0] * pic.mana.size[1])
#     manbc=manb.getcolors(pic.manb.size[0] * pic.manb.size[1])
#     manqc=manq.getcolors(pic.manq.size[0] * pic.manq.size[1])
# 
# 
#     for i in range(5):
#         k=picture[i].getcolors(picture[i].getcolors(picture[i].size[0]*picture[i].size[1]))
#         if k==cbaac:
#             servant.append('cba')
#             cards.append('a')
#         elif k==cbabc:
#             servant.append('cba')
#             cards.append('b')
#         elif k==cbaqc:
#             servant.append('cba')
#             cards.append('q')
#         elif k==cbasac:
#             servant.append('cba')
#             cards.append('a')
#         elif k==cbasbc:
#             servant.append('cba')
#             cards.append('b')
#         elif k==cbasqc:
#             servant.append('cba')
#             cards.append('q')
#         elif picture[i].getcolors()==mana.getcolors():
#             servant.append('man')
#             cards.append('a')
#         elif picture[i].getcolors()==manb.getcolors():
#             servant.append('man')
#             cards.append('b')
#         elif picture[i].getcolors()==manq.getcolors():
#             servant.append('man')
#             cards.append('q')
#         print(servant)
#         print(cards)
#             
#     print('1  2  3  4  5')
#     print(servant)
#     print(cards)
#     time.sleep(5)
#     
#     First,Second=choose.play_cards(servant,cards)
#     
#     return First,Second
# 
#
def times(k):
    start = time.perf_counter()
    for i in range(k + 1):
        a = '*' * i
        b = '.' * (k - i)
        c = (i / k) * 100
        dur = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end='')
        time.sleep(1)

    print("\n")

def emailme():
    sender='1052820731@qq.com'
    receiver='1052820731@qq.com'
    password='nqqgghounyxqbfhb'
    mail_host = "mail.qq.com"
    message=email.mime.text.MIMEText('DAD,CHECK PLEASE!','plain','utf-8')
    message['From']=email.header.Header('YOUR SON','utf-8')
    message['To']=email.header.Header('FATHER WJ','utf-8')
    subject='FGO'
    message['Subject']=email.header.Header(subject,'utf-8')

    ME = smtplib.SMTP()
    ME.connect(host=mail_host, port=25)
    ME.ehlo()  # 向邮箱发送SMTP 'ehlo' 命令
    ME.starttls()
    ME.login(sender,password)
    ME.sendmail(sender, receiver, message.as_string())
    ME.quit()
    print ("ECPECTING DADY!")

