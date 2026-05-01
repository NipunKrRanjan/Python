from fastapi import FastAPI
import json

def load_data():
    with open('genre_mapping.json',"r") as f:
        data=json.load(f)
        print(data)
    return data

app=FastAPI()

@app.get("/")
def intro():
    return {"Welcome to Movie View System"}

@app.get("/about")
def about():
    return {"Shows the JSON file named genre"}

@app.get("/view")
def view():
    data=load_data()
    return data