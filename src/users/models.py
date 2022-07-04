from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, sql
from sqlalchemy.orm import relationship

from db import Base


class User(Base):

    __tablename__ = 'user_user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True, nullable=True)
    hashed_password = Column(String, nullable=False)
    date_join = Column(DateTime(timezone=True), server_default=sql.func.now())
    last_active = (Column(DateTime)) 
    avatar = Column(String)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    books = relationship("Book", back_populates="owner")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user_user.id"))
    owner = relationship("User", back_populates="books")