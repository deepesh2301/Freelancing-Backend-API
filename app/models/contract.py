from __future__ import annotations
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class Contract(Base):
    __tablename__ = "contracts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id"),
        unique=True,
        nullable=False
    )

    client_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    freelancer_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="Active"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    project = relationship(
        "Project",
        back_populates="contract"
    )

    client = relationship(
        "User",
        foreign_keys=[client_id],
        back_populates="client_contracts"
    )

    freelancer = relationship(
        "User",
        foreign_keys=[freelancer_id],
        back_populates="freelancer_contracts"
    )

    payment = relationship(
        "Payment",
        back_populates="contract",
        uselist=False
    )

    proposal_id : Mapped[int] = mapped_column(
        ForeignKey("proposals.id"),
        unique=True,
        nullable= False
    )

    proposal = relationship(
        "Proposal",
        back_populates="contract"
    )

    reviews = relationship("Review", back_populates="contract")

    