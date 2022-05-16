from collections import UserList
import enum
from sqlalchemy import Column, Boolean, Integer, String, Enum, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..db_config import Base
from .mixins import Timestamp


class Todo(Timestamp, Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String(50), nullable=False)
    details = Column(Text, nullable=True)
    is_done = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    owner = relationship('User', back_populates='todo')