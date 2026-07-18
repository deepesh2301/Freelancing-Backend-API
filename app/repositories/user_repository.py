from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from app.models.user import User
# from app.models.role import Role


class UserRepository:

    def __init__(self, db:Session):
        self.db=db

    def get_by_email(self, email:str):
        return (self.db.query(User)
                .options(joinedload(User.role))
                .filter(User.email==email)
                .first()
                )
    
    def get_by_phone(self, phone:str):
        return self.db.query(User).filter(User.phone==phone).first()

    def create_user(self, user:User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    # def get_all_roles(self):
    #     return self.db.query(Role).filter(Role.name!="Admin").all()