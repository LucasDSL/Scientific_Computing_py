import urllib.request, urllib.error, urllib.parse 
from bs4 import BeautifulSoup
import ssl
from urllib.request import Request, urlopen

# Ignore SSL certificate errors 
ctx = ssl.create_default_context()
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
# The scripts pretends to be a differente browser so its not bloked by a website
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all anchor tags 
tags = soup('p')
print(len(tags))