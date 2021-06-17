import requests
import sys

#Check Status code
def status_check(response):
    try:
        if response.status_code == 200:
            print("The Status Code is =" , response.status_code);
            return True;
        elif response.status_code == 401:
            print("Status code is=", response.status_code," Blacklisted From server")
            return False
        elif response.status_code == 404:
            print("Page not found")
            return "Ended"
        else:
            print("Status code is =",response.status_code,"Please Check the status code")
            return False
    except:
        print("Something Wrong Happened");
        exit()
#Increase page count and call copy to html
def increment_page():
    proxylist = {
        "https":"37.120.169.116:8080",
    }
    url = "https://www.mrpcgamer.com/category/pc-games/page/"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
    for x in range(sys.stdout**sys.maxsize):
        increment_string = url + str(x) + "/"
        response = requests.get(increment_string,headers=headers,proxies=proxylist)
        if status_check(response) == True:
            copy_html(x,response)
        elif status_check(response) == "Ended":
            return("Page ended")
        else:
            print("Banned")

#Copy the Html to local PC
def copy_html(val,response):
   f=open("./pages/"+str(val)+".html","wb")
   f.write(response.content)
   f.close()
    
increment_page();