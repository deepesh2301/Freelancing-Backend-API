from __future__ import annotations
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base

class Project(Base):
    __tablename__="projects"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    title: Mapped[str] = mapped_column(String(150), nullable=False)

    description: Mapped[str] = mapped_column(Text, nullable= False)

    budget: Mapped[str] = mapped_column(String(30), default="open")

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    client_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable= False)

    client :Mapped["User"] = relationship("User", back_populates="projects")

    proposals: Mapped[list["Proposal"]]= relationship(
        back_populates="project"
    )

    contract: Mapped["Contract"] = relationship(
        "Contract",
        back_populates="project",
        uselist=False
)