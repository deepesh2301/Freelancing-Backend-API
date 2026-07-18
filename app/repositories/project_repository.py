from sqlalchemy.orm import Session

from app.models.project import Project

class ProjectRepository:

    def __init__(self, db:Session):
        self.db = db

    
    def create_project(self, project:Project):
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project
    
    def get_all_projects(self):
        return self.db.query(Project).all()
    

    def get_project_by_id(self, project_id:int):
        return (
            self.db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )
    
    def update_project(self,db_project):
        self.db.commit()
        self.db.refresh(db_project)
        return db_project
    
    
    def delete_project(self,project):
        self.db.delete(project)
        self.db.commit()

        return {
            "message":"Project deleted successfully"
        }
        
    
    def get_project_by_client(self, client_id):
        return(
            self.db.query(Project)
            .filter(Project.client_id == client_id)
            .all()
        )