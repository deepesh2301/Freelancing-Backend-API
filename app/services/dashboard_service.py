from app.repositories.project_repository import ProjectRepository
from app.repositories.proposal_repository import ProposalRepository
from app.repositories.contract_repository import ContractRepository
from app.repositories.payment_repository import PaymentRepository
from app.repositories.review_repository import ReviewRepository

class DashboardService:

    def __init__(self,db):
        self.project_repository = ProjectRepository(db)
        self.proposal_repository = ProposalRepository(db)
        self.contract_repository = ContractRepository(db)
        self.payment_repository = PaymentRepository(db)
        self.review_repository = ReviewRepository(db)

    
    def get_dashboard(self, current_user):

        #  Client dashboard 

        if current_user.role.name == "Client":

            projects = self.project_repository.get_project_by_client(current_user.id)

            contracts = self.contract_repository.get_by_client(current_user.id)

            payments = self.payment_repository.get_by_user(current_user.id)

            return {
                "role":"Client",

                "total_project" :len(projects),

                "active_contract":
                    len([c for c in contracts if c.status =="Active"]),

                "completed_contracts":
                    len([c for c in contracts if c.status =="Completed"]),
               
                "total_payment":
                    sum(p.amount for p in payments) 
            }
        
        # ---------------- FREELANCER DASHBOARD ---------------- #

        proposals = self.proposal_repository.get_by_freelancer(current_user.id)

        contracts = self.contract_repository.get_by_freelancer(current_user.id)

        payments = self.payment_repository.get_by_user(current_user.id)

        rating = self.review_repository.get_average_rating(current_user.id)

        return{
            "role": "Freelancer",

            "total_proposals": len(proposals),

            "accepted_proposals":
                len([p for p in proposals if p.status =="Accepted"]),

            "active_contracts":
                len([c for c in contracts if c.status =="Active"]),
            
            "total_earnings":
                sum(float(p.amount for p in payments)),

            "average_rating":
                round(rating,2) if rating else 0
        }
