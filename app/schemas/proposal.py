from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ProposalCreate(BaseModel):
    cover_letter: str
    bid_amount: str

class ProposalResponse(BaseModel):
    id: int
    cover_letter: str
    bid_amount: str
    status: str
    created_at: datetime
    freelancer_id: int
    project_id: int

    model_config = ConfigDict(from_attributes=True)