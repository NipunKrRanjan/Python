from fastapi import FastAPI

# Initialize the app
app = FastAPI()

@app.get("/")
def hello():
    return {"Hello": "World"}

@app.get("/about")
def about():
    return{"This is an about page"}