from pydantic import BaseModel,field_validator,computed_field,Field
from fastapi import FastAPI,HTTPException,Path
from fastapi.responses import JSONResponse
from typing import Optional,List,Dict,Annotated,Literal
import pickle
import pandas as pd

app=FastAPI()

with open(r'Model.pkl','rb') as f:
    model_used=pickle.load(f)

class Input_Class(BaseModel):
    sepal_length:Annotated[float,Field(...,description="Enter the sepal length")]
    sepal_width:Annotated[float,Field(...,description="Enter the sepal width")]
    petal_length:Annotated[float,Field(...,description="Enter the petal length")]
    petal_width:Annotated[float,Field(...,description="Enter the petal width")]

FEATURE_ORDER = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

#Converting class to DataFrame
@app.post("/predict")
def prediction(Input:Input_Class):
    input_df = pd.DataFrame([Input.model_dump()])
    input_df = input_df[FEATURE_ORDER]

    prediction=model_used.predict(input_df)[0]

    return JSONResponse(status_code=200,content={"Predicted Species":str(prediction)})
