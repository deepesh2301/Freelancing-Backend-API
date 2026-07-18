from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.user import User
from app.schemas.review import ReviewCreate
from app.services.review_service import ReviewService
from app.utils.dependencies import get_current_user

router = APIRouter(
    prefix="/reviews",
    tags=["/Reviews"]
)

@router.post("/{contract_id}")
def create_review(
    contract_id:int,
    review:ReviewCreate,
    db:Session = Depends(get_db),
    current_user:User = Depends(get_current_user)
):
    review_service = ReviewService(db)

    return review_service.create_review(
        contract_id,
        review,
        current_user
    )


@router.get("/my")
def get_my_reviews(
    db:Session = Depends(get_db),
    current_user:User=Depends(get_current_user)
):
    review_service = ReviewService(db)

    return review_service.get_my_reviews(current_user)