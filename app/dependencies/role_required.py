from fastapi import Depends, HTTPException, status

from app.utils.dependencies import get_current_user
from app.models.user import User

def require_role(allowed_roles: list):

    def role_checker(current_user:User = Depends(get_current_user)):

        if current_user.role.name not in allowed_roles:
            raise HTTPException(
                status_code= status.HTTP_403_FORBIDDEN,
                detail="You don't have permission to accesss this resource"
            )
        
        return current_user
    return role_checker