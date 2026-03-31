def create_file(name):
    with open("output.txt","w") as f:
        f.write(name)
    return {"file": "created"}
