import requests
import json
import bs4 as BeautifulSoup

class Gamescrape():
    def __init__(self) -> None:
        soup = BeautifulSoup

    def open_links(self): # Function to add links to be scraped
        with open("./links3.json","r") as f:
            allgamelinks = json.loads(f)

    def scrape_title(self, url):
        pass

game = Gamescrape()
