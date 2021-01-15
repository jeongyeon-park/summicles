import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import operator
import time
import datetime
from konlpy.tag import Komoran


def get_news(sectionid, date):
    url = "https://news.naver.com/main/ranking/popularDay.nhn?mid=etc&sid1=111"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    l = []
    ranking_text = soup.find_all(class_='ranking_text')
    for item in ranking_text:
        d = {}
        d['LinkSrc'] = item.find('a')['href']
        d['Title'] = item.find('a')['title']
        d['Views'] = item.find(class_="ranking_view").get_text()
        l.append(d)

    for link in l:
        resp = requests.get("http://news.naver.com" + link['LinkSrc'])
        soup = BeautifulSoup(resp.text, "html.parser")
        content = soup.find(id="articleBodyContents")
        link['Content'] = clean_text(content)

    df = pd.DataFrame(l)
    return df


def clean_text(text):
    content = text.get_text()
    cleaned_text = re.sub('[a-zA-Z]', '', content)
    cleaned_text = cleaned_text.replace("오류를 우회하기 위한 함수 추가", "")
    cleaned_text = cleaned_text.replace("동영상 뉴스 오류를 우회하기 위한 함수 추가", "")
    cleaned_text = cleaned_text.replace("무단전재 및 재배포 금지", "")
    return cleaned_text


get_news(100, 20210115)
