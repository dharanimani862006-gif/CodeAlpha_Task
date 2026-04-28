import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# Function to get webpage content
def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print("Error fetching page:", e)
        return None


# Function to extract book details
def extract_books(html):
    soup = BeautifulSoup(html, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    book_data = []

    for book in books:
        try:
            title = book.h3.a["title"]

            price = book.find("p", class_="price_color").text

            rating = book.find("p")["class"][1]

            availability = book.find("p", class_="instock availability").text.strip()

            book_data.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Availability": availability
            })

        except Exception as e:
            print("Error parsing book:", e)

    return book_data


# Main function
def main():
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    
    all_books = []

    print("🔄 Starting book scraping...")

    # Scrape multiple pages
    for page in range(1, 4):   # 3 pages scrape pannum
        print(f"📄 Scraping page {page}...")

        url = base_url.format(page)
        html = fetch_page(url)

        if html:
            books = extract_books(html)
            all_books.extend(books)

        time.sleep(2)   # delay to act like human

    # Convert to DataFrame
    df = pd.DataFrame(all_books)

    # Save to CSV
    df.to_csv("books_advanced.csv", index=False, encoding="utf-8-sig")

    print("✅ Scraping completed! Data saved as books_advanced.csv")


# Run program
if __name__ == "__main__":
    main()