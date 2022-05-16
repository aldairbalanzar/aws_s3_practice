from collections import UserList
import enum
from sqlalchemy import Column, Boolean, Integer, String, Enum, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..db_config import Base
from .mixins import Timestamp


class Role(enum.Enum):
    restaurant_manager = 1
    restaurant_cook_expo = 2
    restaurant_server = 3

class User(Timestamp, Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Enum(Role))
    img_url = Column(String)

    Todo = relationship('Todo', back_populates='owner')