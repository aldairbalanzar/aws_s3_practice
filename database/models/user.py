import enum
from sqlalchemy import Column, Boolean, Integer, String, Enum, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..db_config import Base


class Role(enum.Enum):
    restaurant_manager = 1
    restaurant_cook_expo = 2
    restaurant_server = 3

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Enum(Role))

    Todo = relationship('Todo', back_populates='owner')

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String(50), nullable=False)
    details = Column(Text, nullable=True)
    is_done = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    owner = relationship('User', back_populates='todo')