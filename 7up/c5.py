# Task
# Web scraping is the practice of extracting data from a website programmatically.

# This is typically done by making an HTTP request to the website to obtain the HTML document markup and parsing the markup to extract the necessary information. Many languages provide libraries which vastly simplify the request and parsing processes.

# In this challenge, your task is to write a function to search a mock bookstore website (Books to Scape) and determine if a title is listed in the store's online inventory.

# in_stock(title, topic)
# Parameters
# title: String - the title of the book to search for

# topic: String - the topic to search in

# Return Value
# Boolean - True if the book is available in this topic category, false otherwise

# You can consider searches, both for topic and title fields, to be exact matches on characters, with one exception: case should be ignored.

# Feel free to research and familiarize yourself with your language's HTML parsing library's documentation. Imports have been added to help get you started, but you may wish to use any other packages available in the challenge environment.


# Thus, a call to

# in_stock("the origin of species", "science")
# should return true; this title is available in the specified topic. Take note of the case-insensitive search.

# On the other hand, a call to

# in_stock("the origin of species", "art")
# should return false, because no such title exists in the Art category.

# Lastly, a search for

# in_stock("Origin of Species", "Science")
# should return false, because "Origin of Species" does not match the actual title, "The Origin of Species".
import unittest
import requests
from bs4 import BeautifulSoup
from typing import List
from enum import Enum
from urllib.parse import urljoin

### UTILS
def clean_text(t: str) -> str:
    return t.lower().strip()

### HTML
def get_soup(url) -> BeautifulSoup:
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")

class CategoryStock:
    # always use lower case
    def __init__(self, category: str, link: str):
        self.category = category
        self.books = []
        self._scrape_books(link)
        print(f"{category} {', '.join(self.books)}")

    def _scrape_books(self, link) -> List[str]:
        """Scrape books of a given page and add to list of books.
        Find next page button and go to the next page to scrape"""
        print("Scraping: ", link)
        
        soup = get_soup(link)
        articles: List[BeautifulSoup] = soup.find_all(
            "article", class_="product_pod")
        books: List[str] = []
        for a in articles:
            if a.name == "article":
                h3 = a.find("h3")
                if h3 is not None :
                    book = h3.find("a")["title"]
                    book = clean_text(book)
                    books.append(book)
        self.books += books
        next_button = soup.find("li", class_="next") 
        if next_button is not None:
            href = next_button.find("a", href=True)["href"]
            next_link = urljoin(link, href)
            self._scrape_books(next_link)

class InvalidInput(Exception):
    pass

class ExceptionType(str, Enum):
    WRONGTOPIC = "Wrong topic name"


def get_all_categories_stock(soup: BeautifulSoup, page: str) -> List[CategoryStock]:
    nav: BeautifulSoup = soup.find("ul", class_="nav nav-list")
    stocks = []
    for item in nav.find("ul").find_all("li"):
        a = item.find("a", href=True) 
        href = a["href"]
        category_name = clean_text(a.text)
        is_valid_category = category_name != ""
        if is_valid_category:
            link = urljoin(page, href)
            category_stock: CategoryStock = CategoryStock(category_name, link)
            stocks.append(category_stock)
    return stocks

url = "http://books.toscrape.com/"
soup: BeautifulSoup = get_soup(url)
# get all categories' stock
stocks: List[CategoryStock] = get_all_categories_stock(soup, page=url)
categories: List[str] = [s.category for s in stocks]
    
def in_stock(title: str, topic: str) -> bool:
    topic = clean_text(topic)
    title = clean_text(title)

    if topic not in categories:
        raise ValueError(ExceptionType.WRONGTOPIC)
    else:
        ind = categories.index(topic)
        return title in stocks[ind].books


# in_stock("the origin of species", "science")
# should return true; this title is available in the specified topic. Take note of the case-insensitive search.

# On the other hand, a call to

# in_stock("the origin of species", "art")
# should return false, because no such title exists in the Art category.

# Lastly, a search for

# in_stock("Origin of Species", "Science")
# should return false

class TestSolution(unittest.TestCase):
    def test_instock(self):
        self.assertEqual(in_stock("A Light in the Attic", "Poetry"), True)
        self.assertEqual(in_stock("the origin of species", "science"), True)
        self.assertEqual(in_stock("the origin of species", "art"), False)
        self.assertEqual(in_stock("Origin of Species", "Science"), False)

if __name__ == "__main__":
    unittest.main()