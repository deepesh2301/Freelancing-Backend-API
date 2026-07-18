from datetime import datetime

from sqlalchemy import DateTime, String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    amount : Mapped[float] = mapped_column(Float, nullable= False)

    payment_method: Mapped[str] = mapped_column(
        String(30), default="UPI"
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="Paid"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    contract_id: Mapped[int] = mapped_column(
        ForeignKey("contracts.id")
    )

    contract = relationship(
        "Contract",
        back_populates="payment"
    )