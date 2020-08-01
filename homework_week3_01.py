import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

#숙제로 내주신 지니뮤직이 안되어서 yes24 best seller 리스트로 했습니다 ㅠ.ㅠ
data = requests.get("http://www.yes24.com/24/Category/BestSeller")
html = BeautifulSoup(data.text, 'html.parser')

items = html.select('div#bestList > ol > li')


for item in items:
    a_tag = item.select_one('a')
    if a_tag is not None:
        title = item.select_one('p:nth-child(3)').text
        writer = item.select_one('.aupu > a').text
        price = item.select_one('.price > strong').text
        review = item.select_one('p:nth-child(6) > a').text
#        print(title, writer, price, review)
        doc = {
            'title': title,
            'writer': writer,
            'price': price,
            'review': review
        }
        db.books.insert_one(doc)
