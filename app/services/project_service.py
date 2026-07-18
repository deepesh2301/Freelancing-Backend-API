from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.project import Project
from app.repositories.project_repository import ProjectRepository
from app.schemas.project import ProjectCreate



class ProjectService:

    def __init__(self,db):
        self.project_repository = ProjectRepository(db)
        

    def create_project(self, project: ProjectCreate, current_user):

        if current_user.role.name !="Client":
            raise HTTPException(
                status_code=403,
                detail="Only clients can create projects"
            )
        
        db_project = Project(
            title = project.title,
            description = project.description,
            budget = project.budget,
            client_id = current_user.id
        )

        return self.project_repository.create_project(db_project)
    

    def get_all_project(self):
        return self.project_repository.get_all_projects()
    

    def get_project_by_id(self, project_id:int):
        project = self.project_repository.get_project_by_id(project_id)

        if not project:
            raise HTTPException(
                status_code=404,
                detail= "Project not found"
            )

        return project
    
    def update_project(self, project_id:int, project,current_user):
        
        db_project = self.project_repository.get_project_by_id(project_id)

        if db_project.client_id !=current_user.id:
            raise HTTPException(
                status_code=403,
                detail="You are not authorized to update this project"
            )
        
        if current_user.role.name != "Client":
            raise HTTPException(
                status_code=403,
                detail="Only clients can update projects"
            )

        if not db_project:
            raise HTTPException(
                status_code=404,
                detail="Project not found"
            )
        
        db_project.title = project.title
        db_project.description=project.description
        db_project.budget = project.budget

        return self.project_repository.update_project(db_project)
    
    def delete_project(self, project_id:int, current_user):
        
        if current_user.role.name != "Client":
            raise HTTPException(
                status_code=403,
                detail="Only Client can delete the project"
            )

        db_project = self.project_repository.get_project_by_id(project_id)

        
        if not db_project:
            raise HTTPException(
                status_code=404,
                detail="Project not found"
            )
        
        if db_project.client_id !=current_user.id:
            raise HTTPException(
                status_code=403,
                detail="You are not authorized to delete this project"
            )

        return self.project_repository.delete_project(db_project)
    