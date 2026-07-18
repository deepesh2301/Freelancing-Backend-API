from  __future__  import annotations
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base



class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    full_name: Mapped[str] = mapped_column(String(100), nullable=False)

    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    phone: Mapped[str] = mapped_column(String(15), unique=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))

    role = relationship("Role", back_populates="users")

    projects: Mapped[list["Project"]] = relationship(
        back_populates="client"
    )

    proposals: Mapped[list["Proposal"]] = relationship(
        back_populates="freelancer"
    )

    client_contracts: Mapped[list["Contract"]] = relationship(
    "Contract",
    foreign_keys="Contract.client_id",
    back_populates="client"
)

    freelancer_contracts: Mapped[list["Contract"]] = relationship(
        "Contract",
        foreign_keys="Contract.freelancer_id",
        back_populates="freelancer"
    )

    reviews_given = relationship(
        "Review",
        foreign_keys="Review.reviewer_id",
        back_populates="reviewer"
    )

    reviews_received = relationship(
        "Review",
        foreign_keys="Review.reviewed_user_id",
        back_populates="reviewed_user"
    )
    
