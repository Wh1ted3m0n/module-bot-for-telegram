from bs4 import BeautifulSoup
import requests
import fake_useragent

#no id
def openNet_parcer():
    link="https://www.opennet.ru/opennews/"
    user = fake_useragent.FakeUserAgent().random
    header = {'user-agent':user}
    
    
    response = requests.get(link,headers=header).text
    soup = BeautifulSoup(response,'lxml')
    table = soup.find('table',class_="ttxt2")
    block = table.find_all("tr")[:3]
    block2 = block[2]
    return block[0].text, block[1].text , f"https://www.opennet.ru{block[1].find("a",class_="s3").get('href')}"
