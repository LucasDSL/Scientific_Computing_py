import urllib.request, urllib.error, urllib.parse 
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = input('Enter url - ')
req = Request(url, headers= {'User-Agent': 'Mozilla/5.0'})
web_page_byte = urlopen(req).read()
web_page = web_page_byte.decode('utf-8')
print(web_page[0:3000])