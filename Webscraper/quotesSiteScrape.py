import requests
from bs4 import BeautifulSoup

html = requests.get("https://quotes.toscrape.com/").text
soup=BeautifulSoup(html,'html.parser')
title = soup.select_one("title").get_text()
quotes = soup.select(".quote")

print(title)

for quote in quotes:
    text=quote.select_one(".text").get_text()
    author=quote.select_one(".author").get_text()
    print(f'{text} - {author}\n')