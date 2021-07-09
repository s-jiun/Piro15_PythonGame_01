import requests
from bs4 import BeautifulSoup
import random
from difflib import SequenceMatcher


class InputError(Exception):
    def __init__(self):
        super().__init__("저기요... 벌써 취하신건 아니죠...? ๑őεő๑ ")


def PrintState():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    print("{0}님은 지금까지 {1}잔을 드셨네요!".format(Me[0], drinks-Me[2]))
    print("치사량까지 {0}잔 만큼 남았습니다.".format(Me[2]))
    print()
    for p in player:
        print("{0}님은 지금까지 {1}잔을 드셨네요!".format(
            player[p][0], drinks-player[p][2]))
        print("치사량까지 {0}잔 만큼 남았습니다.".format(player[p][2]))
        print()
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")


def checkWinner1(p, randomTitle, randomSinger):
    if SequenceMatcher(None, randomSinger, songList[randomTitle]).ratio() >= 0.3:
        player[p][1] = 'W'
    else:
        player[p][1] = 'L'
        player[p][2] -= 1


def Turn(currentPlayer):
    currentPlayer = turn[turn.index(currentPlayer) + 1]


playerList = [{'player1': ["민지", 'L', 0]}, {'player1': ["민지", 'L', 0], 'player2':["지운", 'L', 0]}, {
    'player1': ["민지", 'L', 0], 'player2':["지운", 'L', 0], 'player3':["성은", 'L', 0]}]

playerName = input("본인의 이름은 :")
turn = [playerName]
print()
print("=======================================================")

print("              본인의 주량을 선택해주세요")
print()
print("              소주 1병은 4잔 입니다")
print()
print("1. 반 병")
print("2. 반 병에서 한 병")
print("3. 한 병에서 한 병 반")
print("4. 한 병 반에서 두 병")
print("5. 두 병 이상")

while True:
    try:
        drinks = int(input("본인의 주량은?:"))
        if drinks > 5 or drinks < 1:
            raise InputError
    except InputError as e:
        print(e)
    else:
        break

drinks *= 2

playerNum = int(input("몇 명과 대결을 하시겠어요? (사회적 거리두기로 인해서 최대 3명을 초대할 수 있습니다) :"))

player = playerList[playerNum - 1]
Me = [playerName, 'L', drinks]

for p in player:
    turn.append(player[p][0])

for p in player.keys():
    player[p][2] = drinks
    print("오늘의 상대는 {0}님 입니다. {0}님의 주량은 {1}잔 입니다.".format(
        player[p][0], player[p][2]))
    print()

PrintState()

currentPlayer = playerName

while True:
    print("   ----------- 게임 리스트 -----------   ")
    print("1. 가수 맞추기")
    print("2. 369 게임")
    print("3. 블랙잭 게임")
    print("지하철 게임")
    print()
    if currentPlayer == turn[0]:
        choice = int(input("당신의 차례입니다. 게임을 골라주세요 : "))
    else:
        choice = int(input("{0}의 차례입니다. {0}은 {1}번을 골랐습니다.".format(
            currentPlayer, random.randint(1, 4))))
    if choice == 1:
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
        winner1 = []

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
            checkWinner1(p, randomTitle, randomSinger)

        print()

        print("정답은?? ★☆  {0} ☆★\n".format(songList[randomTitle]))

        if SequenceMatcher(None, answer, songList[randomTitle]).ratio() >= 0.3:
            print("ᕕ( ᐛ )ᕗ  성공~ ᕕ( ᐛ )ᕗ")
            Me[1] = 'W'
            winner1.append(playerName)
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
                winner1.append(player[p][0])
            else:
                continue

        if len(winner1) > 0:
            for i in range(len(winner1)):
                print(winner1[i], end='')
            print(" 빼고 한 잔 해~")
        else:
            print("모두 한 잔 해~")
        Turn(currentPlayer)
        PrintState()

    elif choice == 2:
        continue
    elif choice == 3:
        continue
    elif choice == 4:
        continue
    else:
        raise InputError
