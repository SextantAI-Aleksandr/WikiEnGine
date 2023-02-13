from typing import Dict, Optional
import json 


def row_json(row: str) -> Dict[str, object]:
    jz = json.loads(row)
    return dict(jz) 


class Article:
    def __init__(self, jz: Dict[str, object]):
        self.title: str = jz['title']
        self.text: str = jz['text']
        self.wikibase_item: Optional[str] = jz.get('wikibase_item', None)


class WikiEngine:
    def __init__(self, jsonpath: str):
        self.jsonpath = jsonpath 
        self.h = open(jsonpath, 'r')

    def next(self) -> Article:
        while True:
            row = self.h.readline()
            if not row:
                yield None 
            jz = row_json(row)
            if not 'title' in jz:
                continue 
            yield Article(jz)
            

if __name__ == '__main__':
    from sys import argv
    key_ct, q, err = {}, 0, 0
    texts = []
    docs = []
    rows = []
    file = argv[1] # 'enwiki-20230206-cirrussearch-content.json' etc.
    print('Reading', file)
    h = open(file, 'r')
    while True:
        row = h.readline()
        rows.append(row)
        if not row:
            break       # stop after the last line 
        q += 1          # increment number of rows processed
        try: 
            jz = row_json(row)
        except Exception as e:
            err += 1 
            print('Error {} with row: {}'.format(e, row) )
            continue
        if 'text' in jz:
            texts.append(jz['text'])
            docs.append(jz)
        for k in jz.keys():
            key_ct[k] = key_ct.get(k, 0) + 1 
        if q % 1000 == 0:
            print('  Processed {:,} rows with {:,} errors  '.format(q, err), end='\r') 


