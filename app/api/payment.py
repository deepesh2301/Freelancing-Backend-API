from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.user import User
from app.schemas.payment import PaymentCreate
from app.services.payment_service import PaymentService
from app.utils.dependencies import get_current_user


router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

@router.post("{/contract_id}")
def create_payment(
    contract_id:int,
    payment:PaymentCreate,
    db:Session = Depends(get_db),
    current_user:User = Depends(get_current_user)
):
    payment_service = PaymentService(db)

    return payment_service.create_payment(
        contract_id,
        payment,
        current_user
    )

@router.get("/my")
def get_my_payment(
    db:Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    payment_service = PaymentService(db)

    return payment_service.get_my_payment(current_user)