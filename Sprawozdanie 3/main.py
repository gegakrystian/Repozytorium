from bs4 import BeautifulSoup
from requests import get
import sqlite3
from sys import argv

URL= 'https://www.olx.pl/oferty/q-bmw-seria-7/'

def p_price (price):
    return float(price.replace(' ', '').replace('zł', '').replace(',','.'))
        

db= sqlite3.connect('baza.db')
cursor=db.cursor()

if len(argv)>1 and argv[1]=='setup':
    cursor.execute('''CREATE TABLE offers (name TEXT, price REAL, city TEXT)''')
    
    
page= get(URL)
bs= BeautifulSoup(page.content, 'html.parser')

for offer in bs.find_all('div', class_='offer-wrapper'):
    footer=offer.find('td', class_='bottom-cell')
    location=footer.find('small', class_='breadcrumb').get_text().strip().split(',')[0]
    title=offer.find('strong').get_text().strip()
    price=p_price(offer.find('p', class_='price').get_text().strip())
    
    cursor.execute('INSERT INTO offers VALUES (?, ?, ?)', (title, price, location))
    db.commit()
    
db.close()

    
   