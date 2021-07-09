import random

def play(player,playerName,startplayer):
    num=1
    final=0
    playerList=[]
    loser=''

    playerList.append(startplayer)
    for p in player.keys():
        playerList.append(player[p][0])
    print('삼~육구 삼육구~! 삼~육구 삼육구~! ')
    while True:
        if final==0:
            for i in range(len(playerList)):

                choice = random.randint(1, 2)
                count = 0
                count += str(num).count('3')
                count += str(num).count('6')
                count += str(num).count('9')

                if(playerList[i]==playerName):  #내 차례!!
                    while True:
                        try:
                            mychoice=input('{} : '.format(playerName))
                            if count==0 and int(mychoice)==num:
                                num+=1
                                break
                            elif count==0 and int(mychoice)!=num:
                                loser=playerList[i]
                                final = 1
                                break
                            elif count>=1 and mychoice.count('짝')==count:
                                num+=1
                                break
                            else:
                                loser = playerList[i]
                                final = 1
                                break
                        except ValueError:
                            print('정수를 입력하세요 ! !')
                    if(loser==playerList):
                        break
                else:   #다른 사람 차례
                    if count==0:
                        print(playerList[i],': ',num)
                    else:
                        print(playerList[i],': ','짝!'*choice)
                        if choice!=count:
                            final=1
                            loser=playerList[i]
                            break
                    num+=1
                if final == 1:
                    break
                else:
                    continue
        elif final==1:
            break
    print(loser, ' 벌주 당첨!')
    return loser
