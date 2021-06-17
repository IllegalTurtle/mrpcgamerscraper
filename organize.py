import bs4
import os
import html5lib
import itertools
import json
#I Like to do things this way alright very un-pythonic of me


class Scrape():
    #Check if a list is numeric
    def listdir_nohidden(self, path) -> None:
        #Init the Values
        self.path = path
        # Gather all the names of files in pages directory and removes the .html
        y = os.listdir(path)
        working_parse_list = [] # Init the x value list 
        for f in y: # Check for hidden and non numeric files
            if f.startswith(".") == True:
                continue
            else:
                working_parse_list.append(f)
        return working_parse_list; #Didnt bother sorting the list since it dosent matter anyway checking for duplicates after wards

    def parse_the_html(self, url): #Parse the HTML and Search for all links with class postimge
        self.url = url
        with open('./pages/'+url,"rb") as htmldoc:
            soup = bs4.BeautifulSoup( htmldoc, "html.parser")
            name_box = soup.findAll("div", attrs={"class":"postimge"})
            hugelist = set()
            for x in name_box:
                   hugelist.add(x.a["href"])
            return hugelist
    def loop_for_all_files_and_json(self, path): #Loop through all the files
        self.path = path;
        biglist= []
        for url in self.listdir_nohidden(path):
            hugelist = self.parse_the_html(url)
            biglist += hugelist
        f = open('links3.json','a')
        jsonobj = json.dumps(biglist, indent=4)
        f.write(jsonobj)
        f.close();
        print("done")

scraping = Scrape()
scraping.loop_for_all_files_and_json("./pages")