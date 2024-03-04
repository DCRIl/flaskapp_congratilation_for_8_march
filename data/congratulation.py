import sqlalchemy

from .db_session import SqlAlchemyBase


class Congratulation(SqlAlchemyBase):
    __tablename__ = 'congratulation'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    text = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
