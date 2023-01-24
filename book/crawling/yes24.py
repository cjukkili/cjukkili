import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time


class Book():
    books = []

    def __init__(self, bookId, title, author, publisher, pubMonth, price, info, index):
        self.id = bookId
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pubMonth = pubMonth
        self.price = price
        self.info = info
        self.index = index

    def __repr__(self):
        return "<Book {}, {}, {}, {}, {}>".format(
            self.title, self.author, self.publisher, self.pubMonth, self.price)

    def __str__(self):
        return "<Book {}, {}, {}, {}, {}>".format(
            self.title, self.author, self.publisher, self.pubMonth, self.price)


def yes24Connect():
    for page in range(1, 50):
        print(page)
        url = f'http://www.yes24.com/24/Category/NewProductList/001?SumGb=04&FetchSize=100&PageNumber={page}'
        res = requests.post(url)
        soup = BeautifulSoup(res.text, 'html5lib')
        tag_name = '#category_layout > tbody > tr'
        books = soup.select(tag_name)
        pageStart = time.time()
        for i in range(0, 200, 2):
            book = books[i].find("td", attrs={"class": "goodsTxtInfo"})
            # 책 이름 및 책 번호 가져오기
            bookInfoTag = 'p:nth-child(1)'
            bookInfos = book.select(bookInfoTag)[0].find("a")
            title = bookInfos.text
            bookUrl = bookInfos['href']
            bookId = int(bookUrl.split('/')[-1])

            # 출판사 및 저자, 가격
            pubInfoTag = 'div > a'
            pubInfo = book.select(pubInfoTag)
            author = book.select('div')[0].text.split('|')[0].strip()
            publisher = book.select('div')[0].text.split('|')[1].strip()
            pubMonth = book.select('div')[0].text.split('|')[2].strip()  # 출판월 추출
            price = book.find("span", attrs={"class": "priceB"}).text

            # 책 정보 및 목차
            detUrl = f'http://www.yes24.com/Product/Goods/{bookId}'
            detRes = requests.post(detUrl)
            detSoup = BeautifulSoup(detRes.text, 'html5lib')
            detInfo = detSoup.find("div", attrs={'class': 'gd_dContLft'})
            index, info = None, None
            if detInfo is not None:
                info = detInfo.find("textarea", attrs={'class': 'txtContentText'})
                index = None
                if info is not None:
                    info = info.text
                index = detInfo.find("div", attrs={'class': 'gd_infoSet gd_infoSetCrop'})
                if index is not None:
                    index = index.find("div", attrs={'class': 'infoWrap_txt'})
                    if index is not None:
                        index = index.text.strip()
            b = Book(bookId, title, author, publisher, pubMonth, price, info, index)
            Book.books.append(b)
        pageEnd = time.time()
        print('page ' + str(page) + ': ' + str(pageEnd - pageStart))


start = time.time()
yes24Connect()
print(len(Book.books))
end = time.time()

print("총시간: " + str(end - start))
