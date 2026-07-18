from fastapi import HTTPException

from app.repositories.contract_repository import ContractRepository


class ContractService:

    def __init__(self, db):
        self.contract_repository = ContractRepository(db)

    def get_my_contracts(self, current_user):
        return self.contract_repository.get_my_contracts(current_user.id)

    def get_contract_by_id(
        self,
        contract_id: int,
        current_user
    ):

        contract = self.contract_repository.get_by_id(contract_id)

        if not contract:
            raise HTTPException(
                status_code=404,
                detail="Contract not found"
            )

        if (
            contract.client_id != current_user.id
            and
            contract.freelancer_id != current_user.id
        ):
            raise HTTPException(
                status_code=403,
                detail="You are not authorized to view this contract."
            )

        return contract

    def complete_contract(
        self,
        contract_id: int,
        current_user
    ):

        contract = self.contract_repository.get_by_id(contract_id)

        if not contract:
            raise HTTPException(
                status_code=404,
                detail="Contract not found"
            )

        if current_user.role.name != "Client":
            raise HTTPException(
                status_code=403,
                detail="Only clients can complete contracts."
            )

        if contract.client_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="You are not authorized to complete this contract."
            )

        if contract.status == "Completed":
            raise HTTPException(
                status_code=400,
                detail="Contract is already completed."
            )

        return self.contract_repository.complete_contract(contract)