from fastapi import FastAPI,Path
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

@app.get("/view/{movie_id}")
def view(movie_id:str=Path(...,description='Enter movie ID')):
    data=load_data()

    if(movie_id in data):
        return data[movie_id]
    return {"Error":"Movie Not Found"}

