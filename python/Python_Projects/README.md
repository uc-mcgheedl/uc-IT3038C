# Project 3 Last FM Top Tracks

Using the LastFM API, I am displaying LastFM's current top tracks. The details include number ranking, song plays, artist name, artist track and LastFM track link. We will be using my API key.

Make sure you have requests installed, if you do not simply type and run this command in your console
```powershell
pip install requests
```
To run, you simply click the run button in your preferred IDE or type this code in the console
```powershell
python.exe .\Project_3.py
```

If you would like to see more tracks simply change the limit in the link then run the program.
```python
r = requests.get('http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key=56f23d13fb8982a333e46b80207e8e9b&limit=10&format=json')
```

The output will look something like this, 
```python
#Example output
# 1  Blinding Lights By The Weeknd Played 4484791 Times 
# Song Link: https://www.last.fm/music/The+Weeknd/_/Blinding+Lights 
# 2  doN'T StArT nOw By Dua Lipa Played 5444354 Times 
# Song Link: https://www.last.fm/music/Dua+Lipa/_/doN%27T+StArT+nOw
# 
```


