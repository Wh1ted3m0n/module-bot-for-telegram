from bs4 import BeautifulSoup
import requests
import fake_useragent


def parcer_habr():
    link = "https://habr.com/ru/flows/develop/articles/"
    user = fake_useragent.FakeUserAgent().random
    header = {'user-agent':user}
    
    
    response = requests.get(link,headers=header).text
    soup = BeautifulSoup(response,'lxml')

    block = soup.find("article",class_="tm-articles-list__item")
    return block.get('id'),block.find_all('span')[2].text,f"https://habr.com{block.find("a",class_="tm-title__link").get('href')}"


