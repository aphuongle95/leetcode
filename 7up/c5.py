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
import requests
from bs4 import BeautifulSoup
from typing import List
from enum import Enum

class CategoryStock():
    # always use lower case
    def __init__(self, category: str, link: str):
      self.category = category
      self.link = link
      self.scrape_articles()
    
    def scrape_articles(self):
      articles: List[str] = self.__getattribute__(self.link)
      self.articles = articles
      
    def _get_articles_from_link(link: str) -> List[str]:
      articles = []
      # TODO scrapes articles
      articles: List[BeautifulSoup] = soup.find_all("article", class_ = "product_pod")
      return articles

class InvalidInput(Exception):
    pass

class ExceptionType(str, Enum):
    WRONGTOPIC = "Wrong topic name"
    
def in_stock(title: str, topic: str) -> bool:
    url = "http://books.toscrape.com/"
    page = requests.get(url)
    soup: BeautifulSoup = BeautifulSoup(page.content, "html.parser")
    # get all categories' stock
    stocks: List[CategoryStock] = get_all_categories_stock(soup)
    categories: List[str] = [s.category for s in stocks]
    if topic.lower not in categories:
      raise ValueError(ExceptionType.WRONGTOPIC)
    else:
      ind = index(topic, categories)
      if title.lower() in stocks[ind].articles:
        return(f"{title} is available in {topic}")
      else:
        return(f"{title} is not available in {topic}")
    
def get_all_categories_stock(soup) -> List[CategoryStock]:
    nav: BeautifulSoup = soup.find("ul", class_ = "nav nav-list")
    stocks = []
    for item in nav.find_all("li"):
        a = item.find('a', href=True)
        link = a['href']
        name = a.text
        category_stock: CategoryStock = CategoryStock(name, link)
        stocks.append(category_stock)
    return stocks