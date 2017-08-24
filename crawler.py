from bs4 import BeautifulSoup
import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
print(list(soup.children))
print(list(soup.children)[1])
html = list(soup.children)[2]
print(html)

print(list(html.children)[3])

para = list(html.children)[3]
print(list(para.children)[1])
x = list(para.children)[1]
print(x.get_text())
