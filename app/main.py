from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.database.database import SessionLocal, Base, engine
from app.seed.seed_roles import seed_roles

from app.api.project import router as project_router
from app.api.auth import router as auth_router
from app.api.proposal import router as proposal_router
from app.api.contract import router as contract_router
from app.api.payment import router as payment_router
from app.api.review import router as review_router
from app.api.dashboard import router as dashboard_router

from app.models.role import Role
from app.models.user import User
from app.models.project import Project
from app.models.proposal import Proposal
from app.models.contract import Contract
from app.models.payment import Payment
from app.models.review  import Review


Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app:FastAPI):
    db = SessionLocal()

    try:
        seed_roles(db)
        print("Default roles seeded successfully. ")
    finally:
        db.close()
    yield
    print("Application Shutdown")

app = FastAPI(lifespan=lifespan)
app.include_router(auth_router)
app.include_router(project_router)
app.include_router(proposal_router)
app.include_router(contract_router)
app.include_router(payment_router)
app.include_router(review_router)
app.include_router(dashboard_router)


@app.get("/")
def home():
    return {"message":"Freelance API Running"}


