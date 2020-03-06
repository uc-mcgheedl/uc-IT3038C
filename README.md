# IT3038C

### LAB 7 

I have created a python script using the plugin flashtext. Flashtext is a python plugin that is used
to find keywords in either files or dictionaries.

First we must install flashtext, so go to VSCode and open a powershell terminal and type this. 

```powershell
pip install flashtext
```
Now, that you have flashtext installed you can perform a multitude of keyword searches. Now in python run this code.
```python
from flashtext import KeywordProcessor
keyword_processor = KeywordProcessor()
```

The previous code imported flashtext and initialized the keyword proccessor. Now we have some options to choose from, like checking the number of keywords in a dictionary, checking if a keyword is present and reading a txt file to look for keywords. Run these examples:

To check the number of keywords in a dictionary
```python
keyword_processor = KeywordProcessor()
keyword_dict = {
    "compliance management": ["HR", "human resources"],
     "product management": ["PM", "product manager"]
 }
keyword_processor.add_keywords_from_dict(keyword_dict)
print(len(keyword_processor))
#output: 4
```
To check if a keyword is present
```python
keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('All Father', 'God')
praise = 'All Father' in keyword_processor
print(praise)
#output: True
jesus = keyword_processor.get_keyword('All Father')
print(jesus)
#output: God
```
Extracts keywords that are in a .txt file (Must have the txt file in the same directory/folder as your code!)
```python
with open('vacation.txt') as sentence:
    content = sentence.read()
keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('Big Apple')
keyword_processor.add_keyword('Bay Area')
print(keyword_processor.extract_keywords(content))
my vacation.txt contained the sentence "i love the Big Apple and the Bay Area."
#output = ['Big Apple', 'Bay Area']
```

Now you know some of flashtext's capabilities!




