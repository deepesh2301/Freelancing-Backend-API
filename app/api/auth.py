from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.database.database import get_db
from app.schemas.user import UserCreate, UserLogin
from app.services.auth_service import AuthService
from app.utils.dependencies import get_current_user
from app.models.user import User
from app.dependencies.role_required import require_role

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.get("/get_all_roles")
def get_all_roles(db:Session=Depends(get_db)):
    aut_service = AuthService(db)

    return aut_service.get_all_roles()


@router.post("/register")
def register(user:UserCreate, db:Session=Depends(get_db)):
    aut_service = AuthService(db)
    created_user = aut_service.register_user(user)


    return {
        "message":"User registered successfully",
        "user_id":created_user.id

    }


@router.post("/login")
def login(from_data:OAuth2PasswordRequestForm = Depends() , db:Session = Depends(get_db)):

    aut_service = AuthService(db)
    
    return aut_service.login_user(from_data)

@router.get("/me")
def get_me(current_user:User = Depends(get_current_user)):
    return current_user


@router.get("/admin")
def admin_dashboard(
    current_user: User = Depends(require_role(["Admin"]))
):
    return {
        "message": "Welcome Admin",
        "user":current_user.full_name
    }

@router.get("/client")
def client_dashboard(
    current_user: User = Depends(require_role(["Client"]))
):
    return {
        "message":"Welcome Client",
        "user": current_user.full_name
    }