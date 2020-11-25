import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase

class Category(SqlAlchemyBase):
    __tablename__ = 'category'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    association_table = sqlalchemy.Table('association', SqlAlchemyBase.metadata,
                                         sqlalchemy.Column('news', sqlalchemy.Integer,
                                                           sqlalchemy.ForeignKey('news.id')),
                                         sqlalchemy.Column('category', sqlalchemy.Integer,
                                                           sqlalchemy.ForeignKey('category.id'))
                                         )