import bs4
import os
import html5lib

#I Like to do things this way alright very un-pythonic of me


class Scrape():
    #Check if a list is numeric
    def listdir_nohidden(self, path) -> None:
        #Init the Values
        self.path = path
        # Gather all the names of files in pages directory and removes the .html
        y = [os.listdir(path)] 
        working_parse_list = [] # Init the x value list 
        for f in y: # Check for hidden and non numeric files
            if f.isnumeric() == False:
                continue
            else:
                working_parse_list.append(f)
        return working_parse_list #Didnt bother sorting the list since it dosent matter anyway checking for duplicates after wards
    def parse_the_html(self, url):
        self.url = url
        with open('./pages'+url,"rb") as htmldoc:
            pass
        soup = bs4.BeautifulSoup(markup=htmldoc, "html.parser")


scraping = Scrape()
