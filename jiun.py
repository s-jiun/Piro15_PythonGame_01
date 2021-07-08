import requests
from bs4 import BeautifulSoup
import random


def checkWinner(player, randomTitle, randomSinger):
    if randomSinger == songList[randomTitle]:
        print("{0} 성공 ٩(ˊᗜˋ*)و ".format(player))
    else:
        print("{0} 실패  (｡•́︿•̀｡) ".format(player))


player1 = "건모"
player2 = "민지"
player3 = "성은"
player4 = "지운"

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
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

randomTitle = random.choice(title)

print("제목: {0}".format(randomTitle))
print("          *****♬ 가수를 맞춰주세요!! ♬*****")
print("** 가수명을 정확하게 입력해주셔야 정답으로 인정됩니다 **")
print()
answer = input("가수는?? ")
print()

randomSinger1 = random.choice(singer)
randomSinger2 = random.choice(singer)
randomSinger3 = random.choice(singer)

print("{0}: {1}".format(player1, randomSinger1))
print("{0}: {1}".format(player2, randomSinger2))
print("{0}: {1}".format(player3, randomSinger3))
print()

print("정답은?? ★☆  {0} ☆★\n".format(songList[randomTitle]))

if answer == songList[randomTitle]:
    print("ᕕ( ᐛ )ᕗ  성공 ᕕ( ᐛ )ᕗ")
else:
    print(" ( ˃̣̣̥᷄⌓˂̣̣̥᷅ )  실패  ( ˃̣̣̥᷄⌓˂̣̣̥᷅ ) ")

print()

checkWinner(player1, randomTitle, randomSinger1)
checkWinner(player2, randomTitle, randomSinger2)
checkWinner(player3, randomTitle, randomSinger3)
