import json
import requests

r = requests.get('http://localhost:3000/')
data=r.json()

widName0 = (data[0]['name'])
widColor0 = (data[0]['color'])
widName1 = (data[1]['name'])
widColor1 = (data[1]['color'])
widName2 = (data[2]['name'])
widColor2 = (data[2]['color'])
widName3 = (data[3]['name'])
widColor3 = (data[3]['color'])

print("%s is %s" %(widName0, widColor0))
print("%s is %s" %(widName1, widColor1))
print("%s is %s" %(widName2, widColor2))
print("%s is %s" %(widName3, widColor3))