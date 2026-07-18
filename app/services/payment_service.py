from fastapi import HTTPException

from app.models.payment import Payment
from app.repositories.payment_repository import PaymentRepository
from app.repositories.contract_repository import ContractRepository
from app.schemas.payment import PaymentCreate


class PaymentService:

    def __init__(self, db):
        self.payment_repository = PaymentRepository(db)
        self.contract_repository = ContractRepository(db)

    def create_payment(
            self,
            contract_id:int,
            payment:PaymentRepository,
            current_user
    ):
        
        # contract exists?
        contract = self.contract_repository.get_by_id(contract_id)

        if not contract:
            raise HTTPException(
                status_code=404,
                detail="Contract not found"
            )
        
        # only client can pay

        if current_user.role.name != "Client":
            raise HTTPException(
                status_code=403,
                detail="Only client can make payments"
            )
        
        # owner check 
        if contract.client_id != current_user.id:
            raise HTTPException(
                status_code=403,
                detail="you are not authorized to pay for this contract"
            )
        
        # Already paid ?
        existing_payment = self.payment_repository.get_by_contract(contract_id)

        if existing_payment:
            raise HTTPException(
                status_code=400,
                detail="Payment already exists"
            )
        
        #  Amount comes from accepted proposal

        amount = contract.proposal.bid_amount

        db_payment = Payment(
            amount=amount,
            payment_method = payment.payment_method,
            status ="Paid",
            contract_id = contract.id
        )
        
        return self.payment_repository.create_payment(db_payment)
    

    def get_my_payment(self, current_user):
        return self.payment_repository.get_my_payment(current_user.id)
