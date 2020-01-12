
#list2 list2
#1 2 3 4 5
#whosecards
#b q a
#cba cbas man

#  reme m bercard           reme n bercolor


def play_cards(servent,cards):
    First = 0
    Second = 0

    # 伯爵无卡时
    def badthinghappened(cards):
        First = -1
        Second = -1
        if 'b' in cards:
            k = cards.index('b')
            First = k
            cards[k] = 'none'
        if 'b' in cards:
            Second = cards.index('b')

        if First == -1:
            if 'a' in cards:
                k = cards.index('a')
                First = k
                cards[k] = 'none'
            if 'a' in cards:
                Second = cards.index('a')
        elif First != -1 and Second == -1:
            if 'a' in cards:
                Second = cards.index('a')

        if Second == -1:
            if 'q' in cards:
                Second = cards.index('q')

        return First, Second

    #有无伯爵卡
    hiscard=0
    remembercard=[]
    remenbercolor=[]
    for i in range(5):
        if servent[i]=='man':
            hiscard+=1
            remembercard.append(i)
            remenbercolor.append(cards[i])

    #伯爵有卡时and没卡时
    if hiscard==0:
        First,Second=badthinghappened(cards)
    elif hiscard==1:
        First=remembercard[0]
        Second =0
        if remembercard[0]==0:
            Second=1
    elif hiscard==2:
        First=remembercard[0]
        Second=remembercard[1]
    else:
        #quick
        if 'q'in remenbercolor:
            k=remenbercolor.index('q')
            First = remembercard[k]
            del remenbercolor[k]
            del remembercard[k]
        if 'q' in remenbercolor:
            Second = remembercard(remenbercolor.index('q'))

        #art
        if First==-1:
            if 'a' in remenbercolor:
                k = remenbercolor.index('a')
                First = remembercard[k]
                del remenbercolor[k]
                del remembercard[k]
            if 'a' in remenbercolor:
                Second = remembercard(remenbercolor.index('a'))
        elif Second==-1 and First!=-1:
            if 'a' in remenbercolor:
                Second = remembercard(remenbercolor.index('a'))


        #buster
            if Second == -1 and First != -1:
                if 'b' in remenbercolor:
                    Second = remembercard(remenbercolor.index('b'))

    if First==-1:
        First==0
    if Second==-1:
        Second=1

    return First,Second


