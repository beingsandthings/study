import requests
from bs4 import BeautifulSoup
import csv

csv_file = open('오렌지_보틀.csv', 'w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['이름', '주소', '전화번호'])
# HTML 코드 받아오기
response = requests.get("https://workey.codeit.kr/orangebottle/index")
# BeautifulSoup 사용해서 HTML 코드 정리
soup = BeautifulSoup(response.text, 'html.parser')

# 모든 지점에 대한 태그 가져오기

for branch_tag in soup.select('div.branch'):
    # 각 태그에서 지점 이름, 전화번호 가져오기
    row = [
        branch_tag.select_one('p.city').get_text(),
        branch_tag.select_one('p.address').get_text(),
        branch_tag.select_one('span.phoneNum').get_text()
    ]
    csv_writer.writerow(row)

# for tag in soup.select('div.branch'):

# 출력 코드

csv_file.close()