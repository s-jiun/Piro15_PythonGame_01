# 변형 블랙잭
# 게임을 선택한 사람은 원하는 카드 갯수를 2~4 중 선택.
# 각 플레이어들은 [A,2,3,4,5,6,7,8,9,10,J,Q,K] 중 원하는 갯수만큼의 카드를 받음.
# 각 카드 숫자의 합이 21이거나 21에 가장 가까운 사람이 승.
# J,Q,K는 10으로 생각하고, Ace는 1로 생각함.
# 카드 숫자의 합이 22 이상일 경우 탈락.
# 네 명 모두 탈락일 경우 다시 진행


import random


playerList = [{'player1': ["민지", 'L', 0]}, {'player1': ["민지", 'L', 0], 'player2':["지운", 'L', 0]}, {
    'player1': ["민지", 'L', 0], 'player2':["지운", 'L', 0], 'player3':["성은", 'L', 0]}]

playerName = input("본인의 이름은 :")
drinks = int(input("본인의 주량은?:"))

drinks *= 2

playerNum = int(input("몇 명과 대결을 하시겠어요? (사회적 거리두기로 인해서 최대 3명을 초대할 수 있습니다) :"))

player = playerList[playerNum - 1]

for p in player.keys():
    player[p][2] = drinks

Me = [playerName, 'L', drinks]


class NotTwoThreeFour(Exception):
    def __init__(self):
        super().__init__('저기요..벌써 취하신 건 아니죠...?')


def card_value(card):
    # J, Q, K는 10으로 생각
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
# 게임 전개가 편리하도록 playerName을 딕셔너리에 넣었습니다. 제 게임만 끝나면 빠지니 걱정하지 않으셔도 됩니다!
player[4] = Me


def blackjack_own():
    while True:
        try:
            card_num = input("➤2~4 중 플레이하길 원하는 카드의 개수를 선택해주세요 : ")
            if not card_num.isdigit():
                raise NotTwoThreeFour
            if int(card_num) != 2 and int(card_num) != 3 and int(card_num) != 4:
                raise NotTwoThreeFour
        except NotTwoThreeFour as e:
            print(e)
        else:
            # 각 플레이어에게 카드 분배
            card_num = int(card_num)
            print("카드 {0}장으로 플레이합니다.".format(card_num))
            for p in player.keys():
                playing_card[player[p][0]] = random.sample(card_deck, card_num)
                # 리스트에 있는 숫자들을 꺼내서 보여주고 싶은데 제 능력 밖입니다...그냥 리스트 자체로 출력합니다..
                print("♠{0}(이)가 뽑은 카드는 {1}입니다.".format(
                    player[p][0], playing_card[player[p][0]]))
                sum_of_card = 0
                # 각 플레이어의 카드 합 구하기
                for i in range(card_num):
                    sum_of_card += card_value(playing_card[player[p][0]][i])
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
                continue
            # 이상이 없을 경우 우승자 결정. 공동 우승 가능.
            else:
                blackjack_result.sort(reverse=True)
                for p in playing_card.keys():
                    if playing_card[p][card_num] == blackjack_result[0]:
                        print("❀❀❀❀❀{0}(이)가 숫자 합 {1}으로 이겼습니다!❀❀❀❀❀".format(
                            p, blackjack_result[0]))
                # player 딕셔너리에 넣었던 playerName 삭제
                del player[4]
                print("게임 종료!")


def blackjack_player():
    while True:
        card_num = random.randint(2, 4)
        # 각 플레이어에게 카드 분배
        card_num = int(card_num)
        print("카드 {0}장으로 플레이합니다.".format(card_num))
        for p in player.keys():
            playing_card[player[p][0]] = random.sample(card_deck, card_num)
            # 리스트에 있는 숫자들을 꺼내서 보여주고 싶은데 제 능력 밖입니다...그냥 리스트 자체로 출력합니다..
            print("♠{0}(이)가 뽑은 카드는 {1}입니다.".format(
                player[p][0], playing_card[player[p][0]]))
            sum_of_card = 0
            # 각 플레이어의 카드 합 구하기
            for i in range(card_num):
                sum_of_card += card_value(playing_card[player[p][0]][i])
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
            continue
        # 이상이 없을 경우 우승자 결정. 공동 우승 가능.
        else:
            blackjack_result.sort(reverse=True)
            for p in playing_card.keys():
                if playing_card[p][card_num] == blackjack_result[0]:
                    print("❀❀❀❀❀{0}(이)가 숫자 합 {1}으로 이겼습니다!❀❀❀❀❀".format(
                        p, blackjack_result[0]))
            # player 딕셔너리에 넣었던 playerName 삭제
            del player[4]
            print("게임 종료!")
