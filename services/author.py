from typing import List

from config import db
from models.author import Author


class AuthorService:
    @staticmethod
    def get_all() -> List[Author]:
        authors = db.session.execute(db.select(Author).order_by(Author.lastname)).scalars()
        return authors

    @staticmethod
    def create(data: dict) -> Author:
        author = Author(
            firstname=data["firstname"],
            lastname=data["lastname"],
        )
        db.session.add(author)
        db.session.commit()
        return author