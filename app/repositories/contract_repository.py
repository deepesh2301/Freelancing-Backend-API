from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.contract import Contract


class ContractRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_contract(self, contract: Contract):
        self.db.add(contract)
        self.db.commit()
        self.db.refresh(contract)
        return contract

    def get_by_project(self, project_id: int):
        return (
            self.db.query(Contract)
            .filter(Contract.project_id == project_id)
            .first()
        )

    def get_by_id(self, contract_id: int):
        return (
            self.db.query(Contract)
            .filter(Contract.id == contract_id)
            .first()
        )

    def update_contract(self, contract: Contract):
        self.db.commit()
        self.db.refresh(contract)
        return contract

    def get_all_contracts(self):
        return self.db.query(Contract).all()
    
    def get_my_contracts(self, user_id:int):
        return (
            self.db.query(Contract)
            .filter(
                or_(
                    Contract.client_id == user_id,
                    Contract.freelancer_id == user_id
                )
            )
            .all()

        )
    
    def complete_contract(self, contract: Contract):
        contract.status = "Completed"
        self.db.commit()
        self.db.refresh(contract)
        return contract
    

    def get_by_client(self, client_id):
        return (
            self.db.query(Contract)
            .filter(Contract.client_id == client_id)
            .all()
        )
    
    def get_by_freelancer(self, freelancer_id):
        return(
            self.db.query(Contract)
            .filter(Contract.freelancer_id == freelancer_id)
            .all()
        )
    