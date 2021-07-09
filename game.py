import random
def mini_369(player):
    num=1
    final=0
    playerList=[]
    for p in player.keys():
        playerList.append(player[p][0])
    print('369게임 시작!')
    while True:
        for i in range(len(playerList)):

            choice = random.randint(1, 2)
            count = 0
            count += str(num).count('3')
            count += str(num).count('6')
            count += str(num).count('9')

            if(playerList[i]==playerName):  #내 차례!!
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
        if final==1:
            break
    print(loser, ' 벌주 당첨!')
    return loser

playerList = [{'player1':["민지",'L', 0]},{'player1':["민지", 'L', 0], 'player2':["지운", 'L', 0]}, {'player1':["민지", 'L', 0], 'player2':["지운", 'L', 0], 'player3':["성은", 'L', 0]}]

playerName = input("본인의 이름은 :")
drinks = int(input("본인의 주량은?:"))

drinks *= 2

playerNum = int(input("몇 명과 대결을 하시겠어요? (사회적 거리두기로 인해서 최대 3명을 초대할 수 있습니다) :"))

player = playerList[playerNum - 1]
print(player)
for p in player.keys():
    player[p][2] = drinks

loser_369=mini_369(player)
print("{0}님이 졌습니다! {0}님이 벌주 한잔을 먹게 됩니다.".format(loser_369))
for p in player.keys():
        if loser_369 in player[p]:
            player[p][2] -= 1




