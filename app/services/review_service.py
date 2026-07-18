from fastapi import HTTPException

from app.models.review import Review
from app.repositories.review_repository import ReviewRepository
from app.repositories.contract_repository import ContractRepository
from app.schemas.review import ReviewCreate


class ReviewService:

    def __init__(self,db):
        self.review_repository = ReviewRepository(db)
        self.contract_repository = ContractRepository(db)


    def create_review(
            self,
            contract_id:int,
            review:ReviewCreate,
            current_user
    ):
        
        # Contract exists?
        contract = self.contract_repository.get_by_id(contract_id)

        if not contract:
            raise HTTPException(
                status_code=404,
                detail="Contract not found"
            )
        
        # contract must be completed
        if contract.status !="Completed":
            raise  HTTPException(
                status_code=400,
                detail="Revies can only be given after contract completion. "
            )
        
        # Reviewer must be part of contract
        if current_user.id not in [contract.client_id, contract.freelancer_id]:
            raise HTTPException(
                status_code=403,
                detail="you are not part of this contract. "
            )
        
        # Already reviewed?

        existing = self.review_repository.get_by_contract_and_review(
            contract.id,
            current_user.id
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail="you have already reviewed this contract. "
            )
        
        
        # Rating validation
        if review.rating < 1 or review.rating > 5:
            raise HTTPException(
                status_code=400,
                detail="Rating must be between 1 and 5."
        )


        if current_user.id == contract.client_id:
            reviewed_user_id = contract.freelancer_id
        else:
            reviewed_user_id = contract.client_id

        db_review = Review(
            contract_id = contract.id,
            reviewer_id = current_user.id,
            reviewed_user_id = reviewed_user_id,
            rating = review.rating,
            comment = review.comment
        )

        return self.review_repository.create_review(db_review)
    

    def get_my_reviews(self, current_user):
        return self.review_repository.get_reviews_for_user(current_user.id)