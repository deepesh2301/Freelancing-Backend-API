from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.review import Review

class ReviewRepository:

    def __init__(self, db:Session):
        self.db = db

    
    def create_review(self, review:Review):
        self.db.add(review)
        self.db.commit()
        self.db.refresh(review)
        return review
    
    def get_by_contract_and_review(
            self,
            contract_id:int,
            reviewer_id:int
    ):
        return(
            self.db.query(Review)
            .filter(
                Review.contract_id == contract_id,
                Review.reviewer_id == reviewer_id
            )
            .first()
        )
    
    def get_reviews_for_user(self, user_id:int):
        return(
            self.db.query(Review)
            .filter(
                Review.reviewed_user_id == user_id
            )
            .all()
        )
    
    def get_all_reviews(self):
        return self.db.query(Review).all()
    

    def get_average_rating(self, user_id):
        return(
            self.db.query(func.avg(Review.rating))
            .filter(Review.reviewed_user_id == user_id)
            .scalar()
        )