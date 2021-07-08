import random
def mini_369(playerList):
    num=1
    final=0
    print('369게임 시작!')
    while True:
        for i in range(len(playerList)):
            choice=random.randint(1,2)
            count=0
            count+=str(num).count('3')
            count += str(num).count('6')
            count += str(num).count('9')

            if count==0:
                print(playerList[i],': ',num)
            else:
                print(playerList[i],': ','짝!'*choice)
                if choice!=count:
                    print(playerList[i],' 벌주 당첨!')
                    final=1
                    break
            num+=1
        if final==1:
            break



#def getStatus():

playerInfo = {"성은":0,"민지":0,"건모":0,"지운":0}  #모든 플레이어 정보
AllPlayers=["성은","민지","건모","지운"]    #모든 플레이어 이름
playerList=[]   #현재 함께 게임 할 플레이어 목록

playerName = input("본인의 이름은 :")
drinks = int(input("본인의 주량은?:"))

playerList.append(playerName)   #자신의 이름을 현재 게임할 플레이어 목록의 첫번째 요소로 추가
me=playerList[0]
playerInfo[me]=drinks   #자신의 주량 설정

print(playerList, playerInfo)

playerNum = int(input("몇 명과 대결을 하시겠어요? (사회적 거리두기로 인해서 최대 3명을 초대할 수 있습니다) :"))

for i in range(0,playerNum):
    if AllPlayers[i]!=me and AllPlayers[i] not in playerList:
        playerList.append(AllPlayers[i])    #나를 제외한 사람중에서 원하는 만큼 현재 게임 플레이어 목록에 추가
    else:
        playerList.append(AllPlayers[i+1])

for i in range(1,len(playerList)):
    playerInfo[playerList[i]]=random.randint(2,6)   #나를 제외한 플레이어의 주량 랜덤 설정

print(playerList, playerInfo)

mini_369(playerList)




