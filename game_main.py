import requests
from bs4 import BeautifulSoup
import random
from difflib import SequenceMatcher
import subway
import mini_369


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


playerInfo = ["민지", "성은", "건모", "지운"]  # 플레이 가능한 모든 플레이어 목록
playerList = []  # 함께 플레이할 플레이어 이름 목록
player = dict()  # 함께 플레이할 플레이어의 정보를 담은 딕셔너리

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

while True:
    playerNum = int(
        input("몇 명과 대결을 하시겠어요? (사회적 거리두기로 인해서 최대 3명을 초대할 수 있습니다) :"))
    if playerNum > 3:
        print("최대 3명까지 초대할 수 있어요!")
    else:
        break
for i in range(playerNum):
    if playerName != playerInfo[i] and playerInfo[i] not in playerList:
        playerList.append(playerInfo[i])
    else:
        playerList.append(playerInfo[i+1])

for i in range(len(playerList)):
    player['player{}'.format(i+1)] = [playerList[i], 'L', 0]

# print(player, playerName)
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
turn_num = -1
while True:
    turn_num += 1
    turn_num = turn_num % len(turn)
    flag = False
    for p in player.keys():
        if player[p][2] == 0:
            print("사람이 죽었어요!")
            print("{0}님이 치사량에 도달했어요!".format(player[p][0]))
            flag = True
    if Me[2] == 0:
        print("사람이 죽었어요!")
        print("{0}님이 치사량에 도달했어요!".format(playerName))
        flag = True
    if flag:
        break
    print("   ----------- 게임 리스트 -----------   ")
    print("1. 가수 맞추기")
    print("2. 369 게임")
    print("3. 블랙잭 게임")
    print("4. 지하철 게임")
    print()
    if turn[turn_num] == playerName:
        choice = int(input("당신의 차례입니다. 게임을 골라주세요 : "))
    else:
        # choice = random.randint(1, 4)
        #####369 test####
        choice = 2
        print("{0}의 차례입니다. {0}은 {1}번을 골랐습니다.".format(
            turn[turn_num], choice))
    if choice == 1:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        req = requests.get(
            'https://www.melon.com/chart/week/index.htm', headers=header)
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
        PrintState()
        continue

    elif choice == 2:
        startplayer = turn[turn_num]
        loser_369 = mini_369.play(player, playerName, startplayer)
        print("{0}님이 졌습니다! {0}님이 벌주 한잔을 먹게 됩니다.".format(loser_369))
        print("술이 들어간다! 쭉!쭉쭉쭉쭉~~쭉!쭉쭉쭉쭉~~ 언제까지 어깨 춤을 추게 할거야~~ 내 어깨를 봐~~ 탈골 됐자나~~~")
        for p in player.keys():
            if loser_369 in player[p]:
                player[p][2] -= 1
        if loser_369 == playerName:
            Me[2] -= 1
        PrintState()
        continue
    elif choice == 3:
        def card_value(card):
            if card in ('J', 'Q', 'K'):
                return int(10)
            elif card in ('2', '3', '4', '5', '6', '7', '8', '9', '10'):
                return int(card)
            elif card == 'Ace':
                return int(1)
        card_deck = ['Ace', '2', '3', '4', '5',
                     '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        playing_card = {}
        blackjack_result = []
        player[4] = Me
        winner3 = []

        def blackjack_own():
            while True:
                try:
                    card_num = input("➤2~4 중 플레이하길 원하는 카드의 개수를 선택해주세요 : ")
                    if not card_num.isdigit():
                        raise InputError
                    if int(card_num) != 2 and int(card_num) != 3 and int(card_num) != 4:
                        raise InputError
                except InputError as e:
                    print(e)
                else:
                    # 각 플레이어에게 카드 분배
                    card_num = int(card_num)
                    print("카드 {0}장으로 플레이합니다.".format(card_num))
                    for p in player.keys():
                        playing_card[player[p][0]] = random.sample(
                            card_deck, card_num)
                        # 리스트에 있는 숫자들을 꺼내서 보여주고 싶은데 제 능력 밖입니다...그냥 리스트 자체로 출력합니다..
                        print("♠{0}(이)가 뽑은 카드는 {1}입니다.".format(
                            player[p][0], playing_card[player[p][0]]))
                        sum_of_card = 0
                        # 각 플레이어의 카드 합 구하기
                        for i in range(card_num):
                            sum_of_card += card_value(
                                playing_card[player[p][0]][i])
                        # 카드 합을 딕셔너리에 추가
                        playing_card[player[p][0]].append(sum_of_card)
                        # 카드 합을 리스트에 추가(후에 21에 가장 가까운 수를 찾기 위해 필요)
                        blackjack_result.append(sum_of_card)
                        print("♣{0}의 카드 숫자의 합은 {1}입니다.".format(
                            player[p][0], playing_card[player[p][0]][card_num]))
                        if sum_of_card > 21:
                            print("아 21이 넘었네요ㅠ 아쉽게 탈락!")
                        elif sum_of_card == 21:
                            print("와우! 블랙잭!꒰໓ ♥ ໕꒱")
                        print("\n")

                    for i in playing_card.keys():
                        # 카드 합이 21이 넘을 경우 blackjack_result 리스트에서 제거
                        if playing_card[i][card_num] > 21:
                            blackjack_result.remove(playing_card[i][card_num])
                    # 모든 플레이어의 카드 숫자 합이 21이 넘을 경우 다시 시작
                    if len(blackjack_result) == 0:
                        print("모든 참가자의 카드 숫자 합이 21이 넘어 다시 시작합니다! 렛츠기릿.")
                        playing_card.clear()
                        continue
                    # 이상이 없을 경우 우승자 결정. 공동 우승 가능.
                    else:
                        blackjack_result.sort(reverse=True)
                        for p in playing_card.keys():
                            if playing_card[p][card_num] == blackjack_result[0]:
                                print("❀❀❀❀❀{0}(이)가 숫자 합 {1}으로 이겼습니다!❀❀❀❀❀".format(
                                    p, blackjack_result[0]))
                                for m in player.keys():
                                    if player[m][0] == p:
                                        player[m][1] = 'W'
                        for p in player:
                            if player[p][1] == 'W':
                                winner3.append(player[p][0])
                            else:
                                player[p][2] -= 1
                                continue
                        # player 딕셔너리에 넣었던 playerName 삭제
                        Me = player[4]
                        del player[4]
                        print("게임 종료!")
                        break

        def blackjack_player():
            while True:
                card_num = random.randint(2, 4)
                # 각 플레이어에게 카드 분배
                card_num = int(card_num)
                print("카드 {0}장으로 플레이합니다.".format(card_num))
                for p in player.keys():
                    playing_card[player[p][0]] = random.sample(
                        card_deck, card_num)
                    # 리스트에 있는 숫자들을 꺼내서 보여주고 싶은데 제 능력 밖입니다...그냥 리스트 자체로 출력합니다..
                    print("♠{0}(이)가 뽑은 카드는 {1}입니다.".format(
                        player[p][0], playing_card[player[p][0]]))
                    sum_of_card = 0
                    # 각 플레이어의 카드 합 구하기
                    for i in range(card_num):
                        sum_of_card += card_value(
                            playing_card[player[p][0]][i])
                    # 카드 합을 딕셔너리에 추가
                    playing_card[player[p][0]].append(sum_of_card)
                    # 카드 합을 리스트에 추가(후에 21에 가장 가까운 수를 찾기 위해 필요)
                    blackjack_result.append(sum_of_card)
                    print("♣{0}의 카드 숫자의 합은 {1}입니다.".format(
                        player[p][0], playing_card[player[p][0]][card_num]))
                    if sum_of_card > 21:
                        print("아 21이 넘었네요ㅠ 아쉽게 탈락!")
                    elif sum_of_card == 21:
                        print("와우! 블랙잭!꒰໓ ♥ ໕꒱")
                    print("\n")

                for i in playing_card.keys():
                    # 카드 합이 21이 넘을 경우 blackjack_result 리스트에서 제거
                    if playing_card[i][card_num] > 21:
                        blackjack_result.remove(playing_card[i][card_num])
                # 모든 플레이어의 카드 숫자 합이 21이 넘을 경우 다시 시작
                if len(blackjack_result) == 0:
                    print("모든 참가자의 카드 숫자 합이 21이 넘어 다시 시작합니다! 렛츠기릿.")
                    playing_card.clear()
                    continue
                # 이상이 없을 경우 우승자 결정. 공동 우승 가능.
                else:
                    blackjack_result.sort(reverse=True)
                    for p in playing_card.keys():
                        if playing_card[p][card_num] == blackjack_result[0]:
                            print("❀❀❀❀❀{0}(이)가 숫자 합 {1}으로 이겼습니다!❀❀❀❀❀".format(
                                p, blackjack_result[0]))
                            for m in player.keys():
                                if player[m][0] == p:
                                    player[m][1] = 'W'
                    for p in player:
                        if player[p][1] == 'W':
                            winner3.append(player[p][0])
                        else:
                            player[p][2] -= 1
                            continue
                    # player 딕셔너리에 넣었던 playerName 삭제
                    Me = player[4]
                    del player[4]
                    print("게임 종료!")
                    break

        if currentPlayer == turn[0]:
            blackjack_own()
        else:
            blackjack_player()

        if len(winner3) > 0:
            for i in range(len(winner3)):
                print(winner3[i], end='')
                print(" 빼고 한 잔 해~")
        else:
            print("모두 한 잔 해~")
        PrintState()
        continue
    elif choice == 4:
        loser = subway.subwayGamestart(
            player, playerName, startplayer=turn[turn_num])
        print("{0}님이 졌습니다! {0}님이 벌주 한잔을 먹게 됩니다.".format(loser))
        for p in player.keys():
            if loser in player[p]:
                player[p][2] -= 1
        if loser == playerName:
            Me[2] -= 1
        PrintState()
    else:
        print("저기요... 벌써 취하신건 아니죠...? ๑őεő๑ ")
        continue
