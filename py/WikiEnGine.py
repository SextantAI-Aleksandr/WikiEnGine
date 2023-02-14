# This library can aid in parsing articles from Wikipedia Cirrus dumps
#
# EXAMPLE USAGE:
# from WikiEnGine import WikiEngine
# wen = WikiEngine('/path/to/enwiki-20230206-cirrussearch-content.json')
# for article in wen.generate():
#     print(article.title)
#     print(article.text)
# 

from typing import Dict, List, Optional
from datetime import datetime
import json 


def row_json(row: str) -> Dict[str, object]:
    jz = json.loads(row)
    return dict(jz) 


class Place:
    def __init__(self, coord: Dict[str, object]):
        # The 'coordinates' field seems to give a list of JSON objects, commonly like this:
        # {'country': 'US', 'coord': {'lon': -112.47583333333334, 'lat': 33.513888888888886}, 'globe': 'earth', 'name': None, 'dim': 30000, 'type': 'adm2nd', 'region': 'AZ', 'primary': True}
        # This class captures the most commonly populated elements 
        self.country: Optional[str] = coord['country']
        self.region: Optional[str] = coord['region']
        self.lat: float = float(coord['coord']['lat'])
        self.lon: float = float(coord['coord']['lon'])


class Article:
    def __init__(self, jz: Dict[str, object]):
        # required properties
        self.page_id: int = int(jz['page_id'])
        self.version: int = int(jz['version'])
        self.created: datetime = datetime.strptime(jz['create_timestamp'],"%Y-%m-%dT%H:%M:%S%z")
        self.updated: datetime = datetime.strptime(jz['timestamp'],"%Y-%m-%dT%H:%M:%S%z")
        self.title: str = jz['title']
        self.text: str = jz['text']
        self.auxiliary_text: str = jz['auxiliary_text']
        self.headings: List[str] = jz['heading']
        self.categories: List[str] = jz['category']
        self.places: List[Place] = [ Place(coord) for coord in jz.get('coordinates', [])]
        self.outgoing_links: List[str] = jz['outgoing_link']
        self.count_incoming_links: int = int(jz.get('incoming_links', 0))
        self.external_links: List[str] = jz['external_link']
        self.redirects: List[str] = [ rd['title'] for rd in jz.get('redirect',[]) ]
        # optional properties
        self.opening_text: Optional[str] = jz.get('opening_text', None) # crawler-style summary
        self.popularity_score: Optional[float] = jz.get('popularity_score', None)
        self.wikibase_item: Optional[str] = jz.get('wikibase_item', None)


class WikiEngine:
    def __init__(self, jsonpath: str):
        self.jsonpath = jsonpath 
        self.h = open(jsonpath, 'r')
        self.q = 0 # number of articles generated
        self.err = 0 # number of errors encountered

    def generate(self) -> Article:
        # create a generator to get all the wikipedia articles
        while True:
            row = self.h.readline()
            if not row:
                yield None # EOF
            try:
                jz = row_json(row)
            except:
                self.err += 1
                print('  WARNING: WikiEngine err # {:,} skipping this non-json row: .'.format(self.err))
                print(row)
                continue 
            if not 'title' in jz:
                continue # only every other row is an article document
            try:
                a = Article(jz)
            except Exception as e:
                print('  WARNING: WikiEngin could not parse an article. Error="{}"'.format(e))
                continue 
            yield a
