from datetime import date
import requests
from bs4 import BeautifulSoup
headers = {
"User-Agent":
"'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'"
}
payload = {'param1': '1', 'param2': '2'}
date = date.today()

today = str(date.year) + '년 ' + str(date.month) + '월 ' + str(date.day) + '일'
now = date.today().strftime('%Y-%m-%d %H:%M:%S')

print("\n       ※ Python Webcrawling Project 1 ※ \n ")
print('   환영합니다, ' + now)
print('      오늘의 주요 정보를 요약해 드리겠습니다.\n')

#날씨 정보 크롤링
wheather = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%82%A0%EC%94%A8&oquery=%EC%BD%94%EB%A1%9C%EB%82%98&tqi=hY0sDdprvOsssAoBxnZssssssMo-373297")
bs_weather = BeautifulSoup(wheather.content,"html.parser")

temperature = bs_weather.select("div.point_box > span.num")
climate = bs_weather.find("span","weather before_slash")
diff = bs_weather.find("span","temperature up")

print(f"서울의 현재 기온은 {temperature[0].text} {climate.text} 어제보다 {diff.text}")
print(" ")

# 뉴스 헤드라인 크롤링
r_news = requests.get("https://news.google.com/topstories?hl=ko&gl=KR&ceid=KR:ko,param=payload,headers=header")
bs_news = BeautifulSoup(r_news.content,"html.parser")

title = bs_news.select("div.xrnccd > article > h3")

news = []

for i in title:
    titles = i.text
    news.append(titles)

print(f"-----{today} 오늘의 헤드라인-----")
print(" ")
for j in range(len(news)):
    print(f"--> {news[j]}")

print(" ")



#코로나 정보 크롤링
corona = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%BD%94%EB%A1%9C%EB%82%98&oquery=%EA%B8%B0%EC%83%81%EC%B2%AD&tqi=hYz%2BlwprvOsssAhZ%2FFlssssssQN-420244")
bs_corona =BeautifulSoup(corona.content,'html.parser')

value = bs_corona.select("div.status_info > ul > li.info_01 > p")
crisis = bs_corona.select("div.status_info > ul > li.info_02 > p")
enter = bs_corona.select("div.status_info > ul > li.info_03 > p")
death = bs_corona.select("div.status_info > ul > li.info_04 > p")

print(f'-----{today}의 코로나 소식 ----- ')
print(' ')
print(f"-->오늘의 신규 확진자 {value[0].text} 명 \n --> 위중증환자 수는 {crisis[0].text} 명  \n  --> 신규 입원은 {enter[0].text} 명  \n   --> 신규 사망 수는 {death[0].text} 명 입니다.")
print(' ')

#음악 정보 크롤링
music= requests.get("https://music.bugs.co.kr/chart")
bs_music =BeautifulSoup(music.content,'html.parser')

song_name = []
artist_name = []

song = bs_music.select("p.title > a")
artist = bs_music.select("p.artist > a")
cnt = 0

for i in range(len(song)):
    song_name.append(song[i].text)
    artist_name.append(artist[i].text)
print(f'-----{today}의 벅스 음원차트 top100-----')
print(' ')
for j in range(0,100):
    if cnt >= 20:
        print("--------------------------------------------------------------------------")
        cnt = 0
    print(f"순위 {j+1}위 - 가수 : {artist_name[j].strip()} - 곡명 : {song_name[j]} ")
    cnt += 1

