from datetime import date
from tkinter import W
import requests
from bs4 import BeautifulSoup

date = date.today()

today = str(date.year) + '년' + str(date.month) + '월' + str(date.day) + '일'
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


#코로나 정보 크롤링
corona = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%BD%94%EB%A1%9C%EB%82%98&oquery=%EA%B8%B0%EC%83%81%EC%B2%AD&tqi=hYz%2BlwprvOsssAhZ%2FFlssssssQN-420244")
bs_corona =BeautifulSoup(corona.content,'html.parser')

value = bs_corona.select("div.status_info > ul > li.info_01 > p")
crisis = bs_corona.select("div.status_info > ul > li.info_02 > p")
enter = bs_corona.select("div.status_info > ul > li.info_03 > p")
death = bs_corona.select("div.status_info > ul > li.info_04 > p")

print(f'-----{today}의 코로나 소식 ----- ')
print(f"확진환자 수는 {value[0].text} 명 위중증환자 수는 {crisis[0].text} 명 \n신규입원은 {enter[0].text} 사망자 수는 {death[0].text} 명 입니다.")
print(' ')

#음악 정보 크롤링
music= requests.get("https://music.bugs.co.kr/chart")
bs_music =BeautifulSoup(music.content,'html.parser')

song_name = []
artist_name = []

song = bs_music.select("p.title > a")
artist = bs_music.select("p.artist > a")

for i in range(len(song)):
    song_name.append(song[i].text)
    artist_name.append(artist[i].text)
print(f'-----{today}의 벅스 음원차트 top100-----')
for j in range(0,100):
    print(f"순위 {j+1}위 - 가수 : {artist_name[j].strip()} - 곡명 : {song_name[j]} ")

