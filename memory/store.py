import json

DB_FILE = "memory.json"

def save_memory(query, result):
    try:
        data = json.load(open(DB_FILE))
    except:
        data = []

    data.append({"query": query, "result": result})
    json.dump(data, open(DB_FILE, "w"))
