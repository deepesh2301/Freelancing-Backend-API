from fastapi import HTTPException

from app.models.proposal import Proposal
from app.repositories.proposal_repository import ProposalRepository
from app.schemas.proposal import ProposalCreate

from app.models.contract import Contract
from app.repositories.contract_repository import ContractRepository
from  app.repositories.project_repository import ProjectRepository



class ProposalService:

    def __init__(self, db):
        self.proposal_repository = ProposalRepository(db)
        self.contract_repository = ContractRepository(db)
        self.project_repository = ProjectRepository(db)

    
    def create_proposal(
            self, 
            project_id: int,
            proposal:ProposalCreate,
            current_user
    ):
        if current_user.role.name != "Freelancer":
            raise HTTPException(
                status_code=403,
                detail="Only freelancers can apply."
        )

        db_project = self.proposal_repository.get_project_by_id(project_id)
        

        if not db_project:
            raise HTTPException(
                status_code=404,
                detail="Project not found"
            )
        
        existing = self.proposal_repository.get_by_project_and_freelancer(
            project_id,
            current_user.id
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail="You have already applied to this project"

            )
        
        db_proposal = Proposal(
            cover_letter = proposal.cover_letter,
            bid_amount = proposal.bid_amount,
            freelancer_id = current_user.id,
            project_id = project_id
        )

        return self.proposal_repository.create_proposal(db_proposal)
    

    def get_my_proposals(self,current_user):

        if current_user.role.name != "Freelancer":
            raise HTTPException(
                status_code=403,
                detail="Only freelancers can view their proposals."
            )
        
        return self.proposal_repository.get_my_proposals(current_user.id)


    def accept_proposal(
            self,
            proposal_id:int,
            current_user
    ):
        db_proposal = self.proposal_repository.get_proposal_by_id(proposal_id)

        if not db_proposal:
            raise HTTPException(
                status_code=404,
                detail="Proposal not found"
            )
        
        if current_user.role.name !="Client":
            raise HTTPException(
                status_code=403,
                detail="Only clients can accept proposals"
            )
        
        if db_proposal.project.client_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="you are not authorized to accept this proposal"
            )
        
        db_proposal.status = "Accepted"

        update = self.proposal_repository.update_proposal(db_proposal)
    
        self.proposal_repository.reject_other_proposals(
            db_proposal.project_id,
            db_proposal.id
        )

        existing_contract = self.contract_repository.get_by_project(
            db_proposal.project_id,
            
        )


        if not existing_contract:

            contract = Contract(
                project_id=db_proposal.project_id,
                proposal_id=db_proposal.id,
                client_id=db_proposal.project.client_id,
                freelancer_id=db_proposal.freelancer_id,
                status="Active"
            )

            self.contract_repository.create_contract(contract)

        return update
        
    

    def get_project_proposals(
        self,
        project_id: int,
        current_user
    ):

        if current_user.role.name != "Client":
            raise HTTPException(
                status_code=403,
                detail="Only clients can view proposals."
            )

        project = self.project_repository.get_project_by_id(project_id)

        if not project:
            raise HTTPException(
                status_code=404,
                detail="Project not found"
            )

        if project.client_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="You are not authorized to view these proposals."
            )

        return self.proposal_repository.get_project_proposals(project_id)

