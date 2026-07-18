from __future__ import annotations
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import  Mapped, mapped_column,relationship

from app.database.database import Base


class Proposal(Base):
    __tablename__ = "proposals"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    cover_letter: Mapped[str] = mapped_column(Text, nullable=False)

    bid_amount: Mapped[str] = mapped_column(String(30), nullable= False)

    status: Mapped[str] = mapped_column(
        String(20),
        default="Pending"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    freelancer_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id")
    )

    freelancer = relationship(
        "User",
        back_populates="proposals"
    )

    project = relationship(
        "Project",
        back_populates="proposals"
    )

    contract = relationship(
        "Contract",
        back_populates="proposal",
        uselist= False
    )