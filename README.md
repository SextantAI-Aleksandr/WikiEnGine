# WikiEnGine

The WikiEnGine library is intended to make it easy to read and parse Wikipedia articles. It uses the CirrusSearch dump files located [here](https://dumps.wikimedia.org/other/cirrussearch/).

**NOTE**: This file has been tested with the recent [enwiki-20230206-cirrussearch-content.json.gz](https://dumps.wikimedia.org/other/cirrussearch/20230206/enwiki-20230206-cirrussearch-content.json.gz) file. Other dates and languages have not been examined.




## Quickstart 

```bash
# Download the CirrusSearch wiki dump:
wget https://dumps.wikimedia.org/other/cirrussearch/20230206/enwiki-20230206-cirrussearch-content.json.gz

# Unzip the file (unzips to ~150 GB)
gzip -dk enwiki*.json.gz

# Clone this repository if you haven't already:
git clone https://github.com/SextantAI-Aleksandr/WikiEnGine

# Incude the WikiEnGine/py folder in your PYTHONPATH
export PYTHONPATH="/path/to/WikiEnGine/py:$PYTHONPATH"
```

Once the dump has been downloaded and unzipped and PYTHONPATH has been set, you can import WikiEnGine like this:

```python
from WikiEnGine import WikiEngine, Article
wen = WikiEngine('/path/to/enwiki-20230206-cirrussearch-content.json')
for article in wen.generate(): # the .generate() method produces a generator
    print(article.title)
    print(article.text)
```



## What other properties are available for articles?

Look at the definition of the Article class [here](https://github.com/SextantAI-Aleksandr/WikiEnGine/blob/main/py/WikiEnGine.py).



## What other dates are available?:

See the list of dates for CirrusSearch dumps here: [https://dumps.wikimedia.org/other/cirrussearch/](https://dumps.wikimedia.org/other/cirrussearch/).

