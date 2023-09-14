from modules.LibraryItem import LibaryItem
from modules.Book import Book
from modules.Magazine import Magazine
from modules.Dvd import Dvd
from modules.Cd import Cd
from modules.Catalog import Catalog
import json

# test class
# item = LibaryItem('Title 1', None, 'Description title 1')
# print(item.title)

# book = Book('isbn', 'Authors', 'Title Book', 'Subject', 'dds_number', 'upc')
# print(book.title)

# magazine = Magazine('Title magazine', 'upc', 'subject', 'volume', 'issue')
# print(magazine.title)

# dvd = Dvd('Dvd Title', 'upc', 'subject', 'actors', 'director', 'genre')
# print(dvd.title)

# cd = Cd('Cd Title', 'upc', 'subject', 'artist')
# print(cd.title)

# test catalog
# input_search = 'test'
# result = Catalog(None).search('test')

# open json file
f = open('files/data.json')
data_json = json.load(f)
# print(data_json)

# create object list
list_book = []
list_magazine = []
list_dvd = []
list_cd = []

# scan/input object from json
for item in data_json:
    if item['source'] == 'book':
        list_book.append(Book(
            title = item['title'],
            subject = item['subject'],
            upc = item['upc'],
            isbn = item['issbn'],
            authors = item['authors'],
            dds_number = item['dds_number']
        ))
    elif item['source'] == 'magazine':
        list_magazine.append(Magazine(
            title = item['title'],
            subject = item['subject'],
            upc = item['upc'],
            volume = item['volume'],
            issue = item['issue']
        ))
    elif item['source'] == 'dvd':
        list_dvd.append(Dvd(
            title = item['title'],
            subject = item['subject'],
            upc = item['upc'],
            actors = item['actors'],
            directors = item['directors'],
            genre = item['genre']
        ))
    elif item['source'] == 'cd':
        list_cd.append(Cd(
            title = item['title'],
            subject = item['subject'],
            upc = item['upc'],
            artist = item['artist']
        ))

# print(list_book)
# print(list_magazine)
# print(list_dvd)
# print(list_cd)

catalog_all = [list_book, list_magazine, list_dvd, list_cd]

while True:
    print('1. Search')
    print('2. Exit')
    choice = input()

    if choice == '1' or choice.lower() == 'search' or choice.lower() == '1. search':
        input_search = input('Search for: ')
        results = Catalog(catalog_all).search(input_search)

        print('=====| results |=====')
        for index, result in enumerate(results):
            print(f'result ke-{index+1} | {result}')
    elif choice == '2' or choice.lower() == 'exit' or choice.lower() == '2. exit':
        print('Program exit')
        break
    else:
        print('Invalid input')

