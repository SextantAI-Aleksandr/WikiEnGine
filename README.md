# WikiEnGine

## Quickstart 

```bash
# set the directory where you want to save the wiki dump files
export WIKI_DIR="/path/to/download/directory" 

# Download the file for a selected year-month-date: 
# See https://dumps.wikimedia.org/other/cirrussearch/
./download.sh YYYYMMDD

# Incude the py folder in your PYTHONPATH
export PYTHONPATH="$PWD/py:$PYTHONPATH"
```

Ensure the file is downloaded and PYTHONPATH has been set. You can then import and use the library like this:

```python
from WikiEnGine import WikiEngine, Article

wen = WikiEngine("/path/to/enwiki-YYYYMMDD-cirrussearch-content.json")
while True:
    article: Article = wen.next()
    
```



## Background and Other resources

Wikipedia is a treasure trove of useful information on a wide variety of topics. There are many different download formats available and different tools for extracting/parsing those. This can make picking an approach difficult. 

[This wiki page](https://en.wikipedia.org/wiki/Wikipedia:Database_download) has a nice description of the varios download files and formats. It says you probably want a file like the one below available from [this page](https://dumps.wikimedia.org/enwiki/)

[https://dumps.wikimedia.org/enwiki/20230201/enwiki-20230201-pages-articles-multistream.xml.bz2](https://dumps.wikimedia.org/enwiki/20230201/enwiki-20230201-pages-articles-multistream.xml.bz2)

But is that really the best choice for your use case?

### Libraries for parsing  enwiki-YYYYMMDD-pages-articles-multistream.xml.bz2 files 

#### WikiExtractor 

The most common library seems to be WikiExtractor (https://github.com/attardi/wikiextractor). It works well for most articles: The text is reasonably clean and preserves paragraphs "\n" and [[links]] to referenced articles. But a surpirsing number of articles have text:"" which is clearly incorrect.

Note this repository also contains functionality for parsing wiki cirrus files (https://dumps.wikimedia.org/other/cirrussearch/20230206/). 

#### PlainTextWikiExtractor 

The PlainTextWikiExtractor (https://github.com/daveshap/PlainTextWikipedia) does not preserve paragraphs or links. It is build on top of WikiTextParse (https://pypi.org/project/wikitextparser/). It dumps each and every article as a id.json file, which makes for a large directory but does help identify them. 

