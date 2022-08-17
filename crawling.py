import requests
from bs4 import BeautifulSoup

# r= requests.get("http://www.naver.com")
# bs = BeautifulSoup(r.content,"html.parser") # html 파서
# # selector= bs.select('.partner_box > .link_partner ') # seloect_one 제일 첫 번째 h3문
# # select 메소드에서 >로 자식 요소를 표현 가능

# selector = bs.find_all("div", {"class" : "partner_box"})


# print(selector) # select 메소드를 사용 할 때에 인덱스를 직접 지정해줘야 함 h3[0].attrs 



r = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8&oquery=%ED%8C%8C%EC%9D%B4%EC%8D%AC&tqi=hYzm0dprvTVssSCa6OlssssstFK-187923")
bs = BeautifulSoup(r.content,"html.parser")

whether = bs.select_one("dl.summary_list > dd.desc")

print('오늘의 체감온도는 {0} 입니다.'.format(whether.text))






