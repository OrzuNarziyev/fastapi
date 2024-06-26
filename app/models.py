from datetime import datetime

from app.database import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, String, Integer, DateTime

class Post(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default_factory=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default_factory=datetime.utcnow)

    title: Mapped[str] = mapped_column(String(256), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)



