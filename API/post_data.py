from pydantic import BaseModel,field_validator,computed_field,Field
from fastapi import FastAPI,HTTPException,Path
from typing import Optional,List,Dict,Annotated,Literal
import os
import json

app=FastAPI()
filename='patient_data.json'

if not os.path.exists(filename) or os.path.getsize(filename) == 0:
    with open(filename, "w") as f:
        json.dump({}, f)


class Address(BaseModel):
    plotno:Annotated[str,Field(...,description="Enter the plot number of patient")]
    city:Annotated[str,Field(...,description="Enter the city of patient")]
    state:Annotated[str,Field(...,description="Enter the state of patient")]

class Patient(BaseModel):
    pid:Annotated[str,Field(...,description="Enter the patient id",example="P001")]
    name:Annotated[str,Field(..., description="Enter name of the patient")]
    gender:Annotated[Literal['male','female','other'],Field(..., description='Gender of the patient')]
    age:Annotated[int,Field(...,gt=0,lt=120,description="Enter age of the patient")]
    address:Annotated[Address,Field(...,description="Enter the address of patient")]
    height:Annotated[float,Field(...,gt=0,description="Enter the height of patient in mteres")]
    weight:Annotated[float,Field(...,gt=0,description="Enter the weight of patient in kgs")]
    allergies:Optional[Annotated[List,Field(description="Enter allregies if any")]]

    @computed_field
    @property
    def bmi(self)->float:
        BMI=self.weight/self.height**2
        return BMI
    
    @computed_field
    @property
    def body(self)->str:
        if(self.bmi<=18.5):
            return 'underweight'
        if(self.bmi<=25):
            return 'normal'
        if(self.bmi<=30):
            return 'overweight'
        return 'obese'

#loading data
def load_data():
    with open(filename,"r") as f:
        data=json.load(f)
        print(data)
    return data

#saving data
def save_data(data):
    with open(filename,"w") as f:
        json.dump(data,f)
    
@app.get('/')
def hello():
    return {"Message":"Welcome to the patient system"}


@app.get('/view')
def view_data():
    data=load_data()
    if(data=={}):
        raise HTTPException(status_code=404,detail="No data available")
    else:
        return data

@app.get('/view_patient/{pid}')
def specific_patient(pid:str=Path(...,description="Enter patient id")):
    if(os.path.getsize(filename=filename)==0):
        raise HTTPException(status_code=404,detail="No data found in file")
    else:
        data=load_data()
        if(pid in data):
            return data[pid]
        else:
            raise HTTPException(status_code=404,detail="Invalid PID")
        

@app.post('/add_patient')
def add_data(patient:Patient):
    pat=patient.model_dump(exclude=['pid'])
    data=load_data()
    data[patient.pid]=pat
    save_data(data)

    raise HTTPException(status_code=200,detail="Patient successfully added")