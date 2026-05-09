from pydantic import BaseModel,field_validator,computed_field,Field
from fastapi import FastAPI,HTTPException,Path
from fastapi.responses import JSONResponse
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
    allergies:Annotated[Optional[List[str]], Field(default=[], description="Enter allergies if any")]

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

#creating a pydantic object for updation of data
class update_data(BaseModel):
    name:Annotated[Optional[str],Field(default=None)]
    gender:Annotated[Optional[Literal['male','female','other']],Field(default=None)]
    age:Annotated[Optional[int],Field(default=None,gt=0,lt=120)]
    address:Annotated[Optional[Address],Field(default=None)]
    height:Annotated[Optional[float],Field(default=None)]
    weight:Annotated[Optional[float],Field(default=None)]
    allergies:Annotated[Optional[List],Field(default=None)]

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

#Updating data based on Pid
@app.put('/update_data/{pid}')
def update_data(updated_info:update_data,pid:str=Path(example="P001")):
    data=load_data()
    if(data=={} or pid not in data):
        raise HTTPException(status_code=404,detail="Patient does not exist")
    existing_info=data[pid]

    updated_data=updated_info.model_dump(exclude_unset=True)

    for key,value in updated_data.items():
        existing_info[key]=value

    #Now we need to recalculate the values of computed fields, so we follow the logic existing_info -> pydantic object of class Patient -> Calculation of computed fields->back to dictionary 
    existing_info['pid']=pid
    existing_info_object=Patient(**existing_info)
    existing_info=existing_info_object.model_dump(exclude={'pid'})
    data[pid]=existing_info
    save_data(data=data)
    return JSONResponse(status_code=200,content={"Message":"Data Updated Successfully"})
    
@app.delete("/delete_data/{pid}")
def delete_user(pid:str=Path(example="P001")):
    data=load_data()
    if(pid not in data):
        raise HTTPException(status_code=404,detail="Patient does not exist")
    if(data=={}):
        raise HTTPException(status_code=404, detail="No data available")
    del data[pid]
    save_data(data)
    return {"Message":"Data Updated Successfully"}
