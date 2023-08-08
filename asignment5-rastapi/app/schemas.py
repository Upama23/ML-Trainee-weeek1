from pydantic import BaseModel

class EmployeePost(BaseModel):
    # id: int
    name: str
    department: str

class EmployeePostReturn(BaseModel):
    id: int
    name: str
    department: str