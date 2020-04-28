#Importing packages
import json
import requests


# Requesting lastfm toptracks url with api key 
r = requests.get('http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key=56f23d13fb8982a333e46b80207e8e9b&limit=10&format=json')
data=r.json()

#Declaring counter
counter = 0

#Iterating through JSON data
for i in data['tracks']['track']:
    artTrack = i["name"] #Artist track
    artName = i['artist']["name"] # Artist name
    pCount = i['playcount'] # Track play count
    tUrl = i['url'] # link to the song on lastFM
    counter += 1 # Counting top tracks
    print('#%s  %s By %s Played %s Times \nSong Link: %s\n ' %(counter,artTrack,artName,pCount,tUrl)) #Printing top tracks
    
  