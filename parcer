import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0'
}
def get_url():
    for count in range(1,3):

        url = f"https://www.cigarpro.ru/drinks/absinthe/?page={count}"

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find_all("div", class_= "product-list__item") #product-list__desc
        for i in data:
            card_url ='https://www.cigarpro.ru' + i.find('a').get('href')
            yield card_url
def array():
    for card_url in get_url():
        response = requests.get(card_url, headers={'User-Agent': 'Mozilla/5.0'})
        sleep(0)
        soup = BeautifulSoup(response.text, "lxml")


        data = soup.find("div", class_="content")
        name = data.find("h1").text
        information = data.find_all("div", class_="product-params__field-content")
        info = []
        for j in information:
            info.append(j.text)
        info_main = ' '.join(info)
        price = data.find("div", class_="product-list__price new").text
        yield name, info_main, price
