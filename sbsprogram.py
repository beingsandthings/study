import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet()
ws.append(['기간', '순위', '프로그램', '시청율'])

for year in range(2010, 2019):
    for month in range(1, 13):
        for weekIndex in range(0, 5):
            url = f"https://workey.codeit.kr/ratings/index?year={year}&month={month}&weekIndex={weekIndex}"
            response = requests.get(url)
            rating_page = response.text
            soup = BeautifulSoup(rating_page, 'html.parser')

            for tr_tags in soup.select('tr')[1:]:
                td_tags = tr_tags.select('td')
                if td_tags[1].get_text() == 'SBS':
                    period = f'{year}년 {month}월 {weekIndex}주차'
                    row = [
                        period,
                        td_tags[0].get_text(),
                        td_tags[2].get_text(),
                        td_tags[3].get_text()
                    ]
                    ws.append(row)


wb.save('SBS_데이터.xlsx')