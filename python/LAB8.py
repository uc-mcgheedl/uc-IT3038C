import requests, re
from bs4 import BeautifulSoup

data  = requests.get("https://acrnm.com/").content 
soup = BeautifulSoup(data, 'html.parser')
j = soup.findAll("div",{"class":"name"})
for x in j :
    
    print(" %s Is a ACROYNM Item " % (x.text))
        
# The output will be ACROYNM'S item names like this
#J1L-GT Is a ACROYNM Item
#J47-GT Is a ACROYNM Item
#J81-WS Is a ACROYNM Item
