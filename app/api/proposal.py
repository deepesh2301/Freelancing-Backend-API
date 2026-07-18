from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.utils.dependencies import  get_current_user
from app.models.user import User
from app.schemas.proposal import ProposalCreate
from app.services.proposal_service import ProposalService


router = APIRouter(
    prefix="/proposals",
    tags=["Proposals"]
)

@router.post("/{project_id}")
def create_proposal(
    project_id: int,
    proposal: ProposalCreate,
    db:Session=Depends(get_db),
    current_user:User =Depends(get_current_user)
):
    proposal_service = ProposalService(db)

    return proposal_service.create_proposal(
        project_id,
        proposal,
        current_user
    )

@router.get("/me")
def get_my_proposals(
    db:Session = Depends(get_db),
    current_user:User = Depends(get_current_user)
):
    proposal_service = ProposalService(db)

    return proposal_service.get_my_proposals(current_user)


@router.get("/project/{project_id}")
def get_project_proposals(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    proposal_service = ProposalService(db)

    return proposal_service.get_project_proposals(
        project_id,
        current_user
    )

@router.put("/{proposal_id}/accept")
def accept_proposal(
    proposal_id:int,
    db:Session = Depends(get_db),
    current_user:User = Depends(get_current_user)
):
    proposal_service = ProposalService(db)
    return proposal_service.accept_proposal(
        proposal_id,
        current_user
    )