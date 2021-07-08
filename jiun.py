import requests
from bs4 import BeautifulSoup
import random
from difflib import SequenceMatcher


def checkWinner(p, randomTitle, randomSinger):
    if SequenceMatcher(None, randomSinger, songList[randomTitle]).ratio() >= 0.3:
        player[p][1] = 'W'
    else:
        player[p][1] = 'L'
        player[p][2] -= 1
        
winner =[]
playerList = [{'player1':["민지",'L', 0]},{'player1':["민지", 'L', 0], 'player2':["지운", 'L', 0]}, {'player1':["민지", 'L', 0], 'player2':["지운", 'L', 0], 'player3':["성은", 'L', 0]}]

playerName = input("본인의 이름은 :")
print()
print("=======================================================")

print("              본인의 주량을 선택해주세요") #이하 주량 선택지 print문 구현 필요

while True:
    drinks = int(input("본인의 주량은?:"))
    if drinks > 5 or drinks < 1:
        print("저기요... 벌써 취하신건 아니죠...? ๑őεő๑ ")
    else:
        break

drinks *= 2

playerNum = int(input("몇 명과 대결을 하시겠어요? (사회적 거리두기로 인해서 최대 3명을 초대할 수 있습니다) :"))

player = playerList[playerNum - 1]

for p in player.keys():
    player[p][2] = drinks
    print("오늘의 상대는 {0}님 입니다. {0}님의 주량은 {1}잔 입니다.".format(player[p][0], player[p][2]))
    print()

Me = [playerName, 'L', drinks]

#각 플레이어의 상태, 게임 선택 코드 작성 필요
#while True, choice 코드로 각 게임 코드 묶어주기

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
req = requests.get('https://www.melon.com/chart/week/index.htm',
                   headers=header)
html = req.text
parse = BeautifulSoup(html, 'html.parser')

titles = parse.find_all("div", {"class": "ellipsis rank01"})
singers = parse.find_all("div", {"class": "ellipsis rank02"})

title = []
singer = []

for t in titles:
    title.append(t.find('a').text)

for s in singers:
    singer.append(s.find('span', {"class": "checkEllipsis"}).text)

songList = dict(zip(title, singer))

print("        *****♬ 노래 제목을 보여드리겠습니다!! ♬*****")
print()

randomTitle = random.choice(title)

print("제목: {0}".format(randomTitle))
print()
print("          *****♬ 가수를 맞춰주세요!! ♬*****")
print("** 가수명을 정확하게 입력해주셔야 정답으로 인정됩니다 **")
print()
answer = input("가수는?? ")
print()


for p in player.keys():
    randomSinger = random.choice(singer)
    print("{0}: {1}".format(player[p][0], randomSinger))
    checkWinner(p, randomTitle, randomSinger)

print()

print("정답은?? ★☆  {0} ☆★\n".format(songList[randomTitle]))

if SequenceMatcher(None, answer, songList[randomTitle]).ratio() >= 0.3:
    print("ᕕ( ᐛ )ᕗ  성공~ ᕕ( ᐛ )ᕗ")
    Me[1] = 'W'
    winner.append(playerName)
else:
    print(" ( ˃̣̣̥᷄⌓˂̣̣̥᷅ )  실패..  ( ˃̣̣̥᷄⌓˂̣̣̥᷅ ) ")
    Me[1] = 'L'
    Me[2] -= 1

print()
for p in player.keys():
    if player[p][1] == 'L':
        print("{0} 실패..  (｡•́︿•̀｡) ".format(player[p][0]))
    else:
        print("{0} 성공~ ٩(ˊᗜˋ*)و ".format(player[p][0]))

for p in player:
    if player[p][1] == 'W':
        winner.append(player[p][0])
    else:
        continue

if len(winner) > 0:
    for i in range(len(winner)):
        print(winner[i], end='')
    print(" 빼고 한 잔 해~")
else:
    print("모두 한 잔 해~")
