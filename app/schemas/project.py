from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProjectCreate(BaseModel):
    title: str
    description: str
    budget: Optional[str] = "Open"

class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    budget: str
    created_at: datetime
    client_id: int

    class Config:
        from_attributes = True


class ProjectUpdate(BaseModel):
    title:str
    description:str
    budget:str