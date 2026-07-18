from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.contract_service import ContractService
from app.utils.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/contracts",
    tags=["Contracts"]
)


@router.get("/my")
def get_my_contracts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    contract_service = ContractService(db)

    return contract_service.get_my_contracts(current_user)


@router.get("/{contract_id}")
def get_contract_by_id(
    contract_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    contract_service = ContractService(db)

    return contract_service.get_contract_by_id(
        contract_id,
        current_user
    )


@router.put("/{contract_id}/complete")
def complete_contract(
    contract_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    contract_service = ContractService(db)

    return contract_service.complete_contract(
        contract_id,
        current_user
    )