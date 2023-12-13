from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from config import db


class Author(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    firstname: Mapped[str] = mapped_column(String(255), nullable=False)
    lastname: Mapped[str] = mapped_column(String(255), nullable=False)
