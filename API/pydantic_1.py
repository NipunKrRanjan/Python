from pydantic import BaseModel,EmailStr,fieldvalidator
from typing import Optional

class Patient(BaseModel):
    name:str
    age:int
    email:EmailStr
    allergies:Optional[str]=None

Patient_info={
    'name':'Nipun',
    'age':30,
    'email':'abc@gmail.com'
}
patient1=Patient(**Patient_info)

def insert(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)

insert(patient1)