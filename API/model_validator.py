from pydantic import BaseModel, EmailStr, model_validator
from typing import Optional

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    allergies: Optional[str] = None
    emergency: Optional[str] = None

    @model_validator(mode='after')
    def check_emergency_needs(self) -> 'Patient':
        # Logic: If elderly, emergency contact is mandatory
        if self.age > 60 and not self.emergency:
            raise ValueError("Add emergency contact for patients over 60")
        return self
    
Patient_info = {
    'name': 'Nipun',
    'age': 30,
    'email': 'abc@gmail.com'
}

# This will succeed
patient1 = Patient(**Patient_info)

def insert(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Email: {patient.email}")

insert(patient1)

# TEST DEBUG: Uncommenting the lines below will raise the ValueError
# old_patient_info = {'name': 'John', 'age': 75, 'email': 'john@test.com'}
# patient2 = Patient(**old_patient_info)