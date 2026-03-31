import json
DB="memory.json"
def store_memory(q,r):
    try: data=json.load(open(DB))
    except: data=[]
    data.append({"q":q,"r":r})
    json.dump(data,open(DB,"w"))
