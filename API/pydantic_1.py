from pydantic import BaseModel,EmailStr,field_validator
from typing import Optional

class Patient(BaseModel):
    name:str
    age:int
    email:EmailStr
    allergies:Optional[str]=None

    @field_validator('name')
    @classmethod
    def name_change(cls,value):
        return value.upper()

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