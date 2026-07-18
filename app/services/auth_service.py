from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserLogin
from app.utils.security import verify_password  
from app.utils.jwt import create_access_token


from app.repositories.user_repository import UserRepository
from app.repositories.role_repository import RoleRepository
from app.schemas.user import UserCreate
from app.models.user import User
from app.utils.security import hash_password


class AuthService:
    def __init__(self, db:Session):
        self.user_repository = UserRepository(db)
        self.role_repository = RoleRepository(db)

    def register_user(self, user:UserCreate):

        # check email exist or not
        existing_email = self.user_repository.get_by_email(user.email)

        if existing_email:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )
        
        existing_phone = self.user_repository.get_by_phone(user.phone)

        if existing_phone:
            raise HTTPException(
                status_code=400,
                detail="Phone number already exists"
            )

        # Hash Password
        hashed_password = hash_password(user.password)

        # create user object
        db_user = User(
            full_name = user.full_name,
            email = user.email,
            password_hash = hashed_password,
            phone = user.phone,
            role_id = user.role_id
        )
         
        # save in databse

        return self.user_repository.create_user(db_user)
    

    def login_user(self, form_data:OAuth2PasswordRequestForm):

        db_user = self.user_repository.get_by_email(form_data.username)

        if not db_user:
            raise HTTPException(
                status_code=400,
                detail="Email not found"
            )
        
        if not verify_password(form_data.password, db_user.password_hash):
            raise HTTPException(
                status_code=400,
                detail="Invaild Password"
            )
        
        access_token = create_access_token(
            data={
                "sub":db_user.email,
                "role":db_user.role.name
                })

        return{
            "access_token":access_token,
            "token_type": "bearer",
            "role":db_user.role.name
        }
    
    def get_all_roles(self):
        return self.role_repository.get_all_roles()
            