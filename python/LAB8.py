import requests, re
from bs4 import BeautifulSoup

data  = requests.get("https://acrnm.com/").content 
soup = BeautifulSoup(data, 'html.parser')
j = soup.findAll("div",{"class":"name"})
for x in j :
    
    print(" %s Is a ACROYNM Item " % (x.text))
        
