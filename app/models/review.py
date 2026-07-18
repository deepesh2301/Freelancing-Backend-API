from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    contract_id: Mapped[int] = mapped_column(
        ForeignKey("contracts.id"),
        nullable=False
    )

    reviewer_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    reviewed_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    rating: Mapped[int] = mapped_column(Integer, nullable=False)

    comment: Mapped[str] = mapped_column(Text, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    contract = relationship(
        "Contract",
        back_populates="reviews"
    )

    reviewer = relationship(
        "User",
        foreign_keys=[reviewer_id],
        back_populates="reviews_given"
    )

    reviewed_user = relationship(
        "User",
        foreign_keys=[reviewed_user_id],
        back_populates="reviews_received"
    )