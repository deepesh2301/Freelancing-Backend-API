from sqlalchemy.orm import Session

from app.models.payment import Payment
from app.models.contract import Contract


class PaymentRepository: 

    def __init__(self, db:Session):
        self.db = db

    def create_payment(self, payment: Payment):
        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)

        return payment
    
    def get_by_contract(self, contract_id:int):
        return(
            self.db.query(Payment)
            .filter(Payment.contract_id == contract_id)
            .first()
        )
    
    def get_my_payment(self, user_id:int):
        return (
            self.db.query(Payment)
            .join(Payment.contract)
            .filter(
                (Payment.contract.has(client_id=user_id)) |
                (Payment.contract.has(freelancer_id=user_id))
            )
            .all()
        )

    
    def get_by_user(self, user_id):
        return(
            self.db.query(Payment)
            .join(Contract)
            .filter(
                (Contract.client_id == user_id) |
                (Contract.freelancer_id == user_id)
                )
            .all()
        )
