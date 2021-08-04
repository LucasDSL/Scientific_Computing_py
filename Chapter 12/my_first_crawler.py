import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup

url = input('Enter url - ')
page = urllib.request.urlopen(url).read()

soup = BeautifulSoup(page, 'html.parser')
for line in soup: 
    print(soup)