import requests
import json
import bs4 as BeautifulSoup

class Gamescrape():

    def open_links(self,url): # Function to add links to be scraped
        with open("./links3.json","r") as f:
            allgamelinks = json.loads(f)
            soup = BeautifulSoup(url, "html.parser")
            # self.game_title(soup)

    def page_title(self, soup): # Get the page title
        title = soup.title
        return title
    
    def game_title(self, soup): # Get the Game titile
        game_title = soup.find("h1" , {"itemprop":"headline"} )
        return game_title
    
    def game_category(self, soup):
        category = soup.find("div",{"class":"labelpost"})
        category_list = category.contents
game = Gamescrape()
