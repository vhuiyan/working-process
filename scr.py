import urllib.request
from bs4 import BeautifulSoup
import io
import csv

def scrap(address, name, agent):
    print(f'Using agent: {agent}')
    request = urllib.request.Request(
        address,
        headers={
            'User-Agent': agent
        }
    )
    page = urllib.request.urlopen(request)
    #print(page)
    soup = BeautifulSoup(page,"html.parser")
    #print(soup)
    #only = soup.find_all("div", attrs={"class" : "whole_wrapper"})
    title = soup.find("div", attrs={"itemprop" : "articleBody"})
    news_name = address.rsplit('/', 1)[1]
    news = ""
    #with io.open('output_news/'+name+'.txt', 'a', encoding='utf-8') as file:
    for i in title.find_all('p'):
        news+=i.text

    print(news)
    with open('data.csv', 'a', newline='') as fp:
        news_name = news_name.replace(u'\xa0', u' ')
        news = news.replace(u'\xa0', u' ')
        news_name = news_name.replace(u'\xa3', u' ')
        news = news.replace(u'\xa3', u' ')
        a = csv.writer(fp, delimiter=',')
        data = [[news_name, news]]
        a.writerows(data)
    return True