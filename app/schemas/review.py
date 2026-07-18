from datetime import datetime

from pydantic import BaseModel, Field


class ReviewCreate(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    comment: str


class ReviewResponse(BaseModel):
    id: int
    contract_id: int
    reviewer_id: int
    reviewed_user_id: int
    rating: int
    comment: str
    created_at: datetime

    class Config:
        from_attributes = True