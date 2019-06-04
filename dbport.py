import tinydb
import re

from tinydb import TinyDB, Query
db = TinyDB('db.json')
doc = Query()

def category(s):
    s = str(s).strip()
    r =  db.search(doc.category == s)
    return r
    
def search(s, usingRE = False):
    if usingRE :
        s = str(s).strip()
    else:
        s = re.escape(str(s).strip())
    r = db.search( doc.intro.search(s) )
    return r

def addItem( item): 
    """item need to be object that have attr: 
       intro , addr , category(optianl)"""
    category = item['category'] if item['category'] else '其他'
    resambleItem = {'intro':item['intro'],'addr':item['addr'],
                    'category': category}
    db.insert(resambleItem)

if __name__ == "__main__":
    print(search('技术'))

