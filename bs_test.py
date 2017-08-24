import requests
from bs4 import BeautifulSoup

req = requests.get('https://en.wikipedia.org/wiki/Cristiano_Ronaldo')

data = req.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
   print(link.get('href'))
