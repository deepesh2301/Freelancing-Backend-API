from sqlalchemy.orm import Session
from app.models.project import Project
from app.models.proposal import Proposal

class ProposalRepository:

    def __init__(self, db:Session):
        self.db = db

    def get_project_by_id(self, project_id):
        return(
            self.db.query(Project)
            .filter(Project.id == project_id).first()
        )

    
    def create_proposal(self, proposal):
        self.db.add(proposal)
        self.db.commit()
        self.db.refresh(proposal)

        return proposal
    
    def get_by_project_and_freelancer(
            self,
            project_id,
            freelancer_id
    ):
        return (
            self.db.query(Proposal)
            .filter(
                Proposal.project_id == project_id,
                Proposal.freelancer_id == freelancer_id
            )
            .first()
        )
    
    def get_my_proposals(self, freelancer_id):
        return(
            self.db.query(Proposal)
            .filter(Proposal.freelancer_id == freelancer_id)
            .all()
        )
    
    def get_proposal_by_id(self,proposal_id):
        return (
            self.db.query(Proposal)
            .filter(Proposal.id == proposal_id)
            .first()
        )
    
    def update_proposal(self, proposal):
        self.db.commit()
        self.db.refresh(proposal)

        return proposal
    
    def reject_other_proposals(
            self,
            project_id:int,
            accepted_proposal_id:id
    ):
        proposals =(
            self.db.query(Proposal)
            .filter(
                Proposal.project_id == project_id ,
                Proposal.id != accepted_proposal_id ,
                Proposal.status =="Pending"
                )
            .all()
        )

        for proposal in proposals:
            proposal.status ="Rejected"

        self.db.commit()

    def get_project_proposals(self, project_id: int):
        return (
            self.db.query(Proposal)
            .filter(Proposal.project_id == project_id)
            .all()
    )

    def get_by_freelancer(self, freelancer_id):
        return (
            self.db.query(Proposal)
            .filter(Proposal.freelancer_id == freelancer_id)
            .all()
        )