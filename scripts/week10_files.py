import json
FILE='data/items.json'

def load():
    try:
        with open(FILE,'r') as f:
            return json.load(f)
    except:
        return []

def save(items):
    with open(FILE,'w') as f:
        json.dump(items,f,indent=4)
