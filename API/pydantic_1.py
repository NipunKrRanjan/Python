from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age:int

Patient_info={
    'name':'Nipun',
    'age':30
}
patient1=Patient(**Patient_info)

def insert(patient:Patient):
    print(patient.name)
    print(patient.age)

insert(patient1)