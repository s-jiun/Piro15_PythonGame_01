# -*- coding: utf-8 -*-
import random
import re


class SubwayRail:
    rail = [
        ["인천역", "동인천역", "도원역", "제물포역", "도화역", "주안역", "간석역", "동암역", "백운역", "부평역", "부개역", "송내역", "중동역", "부천역", "소사역", "역곡역", "온수역", "오류동역", "개봉역", "구일역", "구로역", "신도림역", "영등포역", "신길역", "대방역", "노량진역", "용산역", "남영역", "서울역", "시청역", "종각역", "종로3가역", "종로5가역", "동대문역", "동묘앞역", "신설동역", "제기동역", "청량리역", "회기역", "외대앞역", "신이문역", "석계역", "광운대역", "월계역", "녹천역", "창동역", "방학역", "도봉역",
            "도봉산역", "망월사역", "회룡역", "의정부역", "가능역", "녹양역", "양주역", "덕계역", "덕정역", "지행역", "동두천중앙역", "보산역", "동두천역", "소요산역", "신창역", "온양온천역", "배방역", "아산역", "쌍용역", "봉명역", "천안역", "두정역", "직산역", "성환역", "평택역", "지제역", "서정리역", "송탄역", "진위역", "오산역", "오산대역", "세마역", "병점역", "세류역", "수원역", "화서역", "성균관대역", "의왕역", "당정역", "군포역", "금정역", "명학역", "안양역", "관악역", "석수역", "금천구청역", "독산역", "가산디지털단지역"],
        ["신정네거리역", "양천구청역", "도림천역", "문래역", "영등포구청역", "당산역", "합정역", "홍대입구역", "신촌역", "이대역", "아현역", "충정로역", "시청역", "을지로입구역", "을지로3가역", "을지로4가역", "동대문역사문화공원역", "신당역", "상왕십리역", "왕십리역", "한양대역", "뚝섬역", "성수역", "신도림역", "까치산역",
         "대림역", "구로디지털단지역", "신대방역", "신림역", "봉천역", "서울대입구역", "낙성대역", "사당역", "방배역", "서초역", "교대역", "강남역", "역삼역", "선릉역", "삼성역", "종합운동장역", "잠실새내역", "잠실역", "잠실나루역", "강변역", "구의역", "건대입구역", "용답역", "신답역", "용두역", "신설동역"],
        ["주엽역", "정발산역", "마두역", "백석역", "대곡역", "화정역", "원당역", "원흥역", "삼송역", "지축역", "구파발역", "연신내역", "불광역", "녹번역", "홍제역", "무악재역", "독립문역", "경복궁역", "안국역", "종로3가역", "을지로3가역", "충무로역",
                "동대입구역", "약수역", "금호역", "옥수역", "압구정역", "신사역", "잠원역", "고속터미널역", "교대역", "남부터미널역", "양재역", "매봉역", "도곡역", "대치역", "학여울역", "대청역", "일원역", "수서역", "가락시장역", "경찰병원역", "대화역", "오금역"],
        ["정왕역", "신길온천역", "안산역", "초지역", "고잔역", "중앙역", "한대앞역", "상록수역", "반월역", "대야미역", "수리산역", "산본역", "금정역", "범계역", "평촌역", "인덕원역", "정부과천청사역", "과천역", "대공원역", "경마공원역", "선바위역", "남태령역", "사당역", "총신대입구역", "동작역",
                "이촌역", "신용산역", "삼각지역", "숙대입구역", "서울역", "회현역", "명동역", "충무로역", "동대문역사문화공원역", "동대문역", "혜화역", "한성대입구역", "성신여대입구역", "길음역", "미아사거리역", "미아역", "수유역", "쌍문역", "창동역", "노원역", "상계역", "오이도역", "당고개역"],
        ["개화산역", "김포공항역", "송정역", "마곡역", "발산역", "우장산역", "화곡역", "까치산역", "신정역", "목동역", "오목교역", "양평역", "영등포구청역", "영등포시장역", "신길역", "여의도역", "여의나루역", "마포역", "공덕역", "애오개역", "충정로역", "서대문역", "광화문역", "종로3가역", "을지로4가역", "동대문역사문화공원역", "청구역",
         "신금호역", "행당역", "왕십리역", "마장역", "답십리역", "장한평역", "군자역", "아차산역", "광나루역", "천호역", "강동역", "둔촌동역", "올림픽공원역", "방이역", "오금역", "개롱역", "거여역", "길동역", "굽은다리역", "명일역", "고덕역", "상일동역", "강일역", "미사역", "하남풍산역", "하남시청역", "방화역", "마천역", "하남검단산역"],
        ["연신내역", "구산역", "응암역", "새절역", "증산역", "디지털미디어시티역", "월드컵경기장역", "마포구청역", "망원역", "합정역", "상수역", "광흥창역", "대흥역", "공덕역", "효창공원앞역", "삼각지역", "녹사평역", "이태원역", "한강진역",
         "버티고개역", "약수역", "청구역", "신당역", "동묘앞역", "창신역", "보문역", "안암역", "고려대역", "월곡역", "상월곡역", "돌곶이역", "석계역", "태릉입구역", "화랑대역", "봉화산역", "불광역", "역촌역", "독바위역", "신내역"],
        ["산곡역", "부평구청역", "굴포천역", "삼산체육관역", "상동역", "부천시청역", "신중동역", "춘의역", "부천종합운동장역", "까치울역", "온수역", "천왕역", "광명사거리역", "철산역", "가산디지털단지역", "남구로역", "대림역", "신풍역", "보라매역", "신대방삼거리역", "장승배기역", "상도역", "숭실대입구역", "남성역", "이수역", "내방역",
                "고속터미널역", "반포역", "논현역", "학동역", "강남구청역", "청담역", "뚝섬유원지역", "건대입구역", "어린이대공원역", "군자역", "중곡역", "용마산역", "사가정역", "면목역", "상봉역", "중화역", "먹골역", "태릉입구역", "공릉역", "하계역", "중계역", "노원역", "마들역", "수락산역", "도봉산역", "석남역", "장암역"],
        ["모란역", "수진역", "신흥역", "단대오거리역", "남한산성입구역", "산성역", "복정역", "장지역", "문정역",
                "가락시장역", "송파역", "석촌역", "잠실역", "몽촌토서역", "강동구청역", "천호역", "암사역"],
        ["김포공항역", "공항시장역", "신방화역", "마곡나루역", "양천향교역", "가양역", "증미역", "등촌역", "염창역", "신목동역", "선유도역", "당산역", "국회의사당역", "여의도역", "샛강역", "노량진역", "노들역", "흑석역", "동작역", "구반포역",
         "신반포역", "고속터미널역", "사평역", "신논현역", "언주역", "선정릉역", "삼성중앙역", "봉은사역", "종합운동장역", "삼전역", "석촌고분역", "석촌역", "송파나루역", "한성백제역", "올림픽공원역", "둔촌오륜역", "개화역", "중앙보훈병원역"]
    ]


class NotInRangeError(Exception):
    pass


def subwayGamestart(player, player_name, startplayer):
    computer = []
    for p in player.keys():
        computer.append(player[p][0])
    print("지하철 게임을 시작합니다!")
    if startplayer in computer:
        rail_num = random.randint(1, 9)
        print("몇호선을 고르시겠습니까?(1~9호선) > ", rail_num)
    else:
        while True:
            try:
                rail_num = input("몇호선을 고르시겠습니까?(1~9호선) > ")
                rail_num = int(rail_num)
                if rail_num < 1 or rail_num > 9:
                    raise NotInRangeError
                else:
                    break
            except ValueError as e:
                print("정수를 입력해주세요!")
            except NotInRangeError as e:
                print("1~9호선 사이를 입력해주세요!")
    rail = SubwayRail.rail[rail_num-1]
    member = computer[:]
    member.append(player_name)
    turn = member.index(startplayer)
    ans_list = []
    while True:
        turn = turn % len(member)
        if turn == 3:
            while True:
                print("{0}호선에 해당하는 역을 말하세요! ex)xx역".format(rail_num))
                ans = input("{0} : ".format(player_name))
                hangul = re.compile('^[가-힣]+$')
                m = hangul.match(ans)
                if not '역' in ans:
                    print("역을 붙여주세요!")
                elif m:
                    break
                else:
                    print("취하셨나요? 정확히 입력해주세요!")

            if ans in rail:
                print("맞았습니다!", end="\n\n\n")
                turn += 1
                ans_list.append(ans)
                rail.remove(ans)
            elif ans in ans_list:
                print("이미 말했습니다!", end="\n\n\n")
                return player_name
            else:
                print("틀렸습니다!", end="\n\n\n")
                return player_name
        else:
            print("{0}호선에 해당하는 역을 말하세요! ex)xx역".format(rail_num))
            prob = random.randint(0, 100)
            if prob <= 20:
                fail_num = random.randint(1, 9)
                while fail_num == rail_num:
                    fail_num = random.randint(1, 9)
                fail_rail = SubwayRail.rail[fail_num-1]
                fail_ans = fail_rail[random.randint(0, len(fail_rail)-1)]
                print("{0} : {1}".format(member[turn], fail_ans))
                print("틀렸습니다!",  end="\n\n\n")
                return member[turn]
            elif prob <= 30:
                fail_ans = ans_list[random.randint(0, len(ans_list)-1)]
                print("{0} : {1}".format(member[turn], fail_ans))
                print("이미 말했습니다!", end="\n\n\n")
                return member[turn]

            else:
                ans = rail[random.randint(0, len(rail)-1)]
                print("{0} : {1}".format(member[turn], ans))
                print("맞았습니다!", end="\n\n\n")
                turn += 1
                ans_list.append(ans)


if __name__ == '__main__':
    playerList = [{'player1': ["민지", 'L', 0]}, {'player1': ["민지", 'L', 0], 'player2':["지운", 'L', 0]}, {
        'player1': ["민지", 'L', 0], 'player2':["지운", 'L', 0], 'player3':["성은", 'L', 0]}]
    playerName = input("본인의 이름은 :")
    while True:
        drinks = int(input("본인의 주량은?:"))
        if drinks > 5 or drinks < 1:
            print("저기요... 벌써 취하신건 아니죠...? ๑őεő๑ ")
        else:
            break
    playerNum = int(
        input("몇 명과 대결을 하시겠어요? (사회적 거리두기로 인해서 최대 3명을 초대할 수 있습니다) :"))
    player = playerList[playerNum - 1]
    drinks *= 2
    for p in player.keys():
        player[p][2] = drinks
        print("오늘의 상대는 {0}님 입니다. {0}님의 주량은 {1}잔 입니다.".format(
            player[p][0], player[p][2]))
    print()
    Me = [playerName, 'L', drinks]
    loser = subwayGamestart(player, playerName, startplayer="건모")
    print("{0}님이 졌습니다! {0}님이 벌주 한잔을 먹게 됩니다.".format(loser))
    for p in player.keys():
        if loser in player[p]:
            player[p][2] -= 1
    for p in player.keys():
        print(player[p])
