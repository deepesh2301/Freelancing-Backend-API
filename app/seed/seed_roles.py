from sqlalchemy.orm import Session
from app.models.role import Role
from app.models.user import User

def seed_roles(db: Session):
    # check if roles already exist
    role = db.query(Role).first()

    if role:
        print("Roles already exist. ")
        return 

    roles = [Role(name="Admin"),
             Role(name="Client"),
             Role(name="Freelancer")
             ]
    
    
    try:
        db.add_all(roles)
        db.commit()
        print("Default roles inserted successfully. ")
    except:
        db.rollback()
        raise

