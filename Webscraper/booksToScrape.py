import requests
from bs4 import BeautifulSoup
import csv

BASE = "https://books.toscrape.com/"

def get_soup(url):
    html = requests.get(url).text
    return BeautifulSoup(html, "html.parser")

file = open("books.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(file)
writer.writerow([
    "Title", "Price", "Stock", "Rating", "Category",
    "UPC", "Image", "Description", "Product Page"
])

current_url = BASE

while True:
    print(f"Scraping page: {current_url}")
    soup = get_soup(current_url)
    
    books = soup.select("article.product_pod")
    
    for book in books:
        title = book.select_one("h3 a")["title"]
        price = book.select_one(".price_color").get_text()
        rating = book.select_one(".star-rating")["class"][1]
        
        img_src = book.select_one("img")["src"].replace("../", "")
        image_url = BASE + img_src
        
        product_href = book.select_one("h3 a")["href"].replace("../", "")
        product_url = BASE + product_href
        
        product_soup = get_soup(product_url)
        
        stock = product_soup.select_one(".instock.availability").get_text(strip=True)
        category = product_soup.select("ul.breadcrumb li a")[-1].get_text()
        
        desc_tag = product_soup.select_one("#product_description + p")
        description = desc_tag.get_text(strip=True) if desc_tag else ""
        
        table_rows = product_soup.select("table tr")
        upc = table_rows[0].select_one("td").get_text()
        
        writer.writerow([
            title, price, stock, rating, category,
            upc, image_url, description, product_url
        ])
        
        print(f"  ✔ Saved: {title}")
    
    next_btn = soup.select_one(".next a")
    if not next_btn:
        print("Finished all pages!")
        break
    
    next_page = next_btn["href"]
    current_url = BASE + "catalogue/" + next_page

file.close()
print("\nAll data saved to books.csv")
