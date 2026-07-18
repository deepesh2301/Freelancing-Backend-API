from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.utils.dependencies import get_current_user
from app.models.user import User
from app.schemas.project import ProjectCreate,ProjectResponse, ProjectUpdate
from app.services.project_service import ProjectService

router = APIRouter(
    prefix="/project",
    tags=["Projects"]
)


@router.post("/", response_model=ProjectResponse)
def create_project(
    project: ProjectCreate,
    db:Session = Depends(get_db),
    current_user: User= Depends(get_current_user)
    ):
    project_service = ProjectService(db)

    return project_service.create_project(project, current_user)

@router.get("/", response_model=list[ProjectResponse])
def get_all_projects(
    db:Session = Depends(get_db)
):
    project_service = ProjectService(db)

    return project_service.get_all_project()


@router.get("/{project_id}", response_model= ProjectResponse)
def get_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    project_service = ProjectService(db)

    return project_service.get_project_by_id(project_id)


@router.put("/updateProject/{project_id}")
def update_project(
    project_id:int,
    project: ProjectUpdate,
    db:Session = Depends(get_db),
    current_user:User = Depends(get_current_user)
):
    project_service = ProjectService(db)

    return project_service.update_project(project_id, project,current_user)


@router.delete("/{project_id}")
def delete_project(
    project_id:int,
    db:Session = Depends(get_db),
    current_user:User = Depends(get_current_user)
):
    project_service = ProjectService(db)

    return project_service.delete_project(project_id,current_user)