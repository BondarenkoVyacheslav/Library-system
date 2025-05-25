# backend/app/models.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Numeric
from sqlalchemy.orm import relationship
from app.db.base import Base

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    author = Column(String(100), nullable=False)
    year = Column(Integer)
    cipher = Column(String(50), unique=True, nullable=False)
    copies = Column(Integer, default=1)
    available = Column(Integer, default=1)
    rating = Column(Numeric(3, 2), default=0.0)
    
    transactions = relationship("Transaction", back_populates="book")

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(100))
    full_name = Column(String(100))
    email = Column(String(100), unique=True)
    role = Column(String(20), default="reader")  # 'reader' или 'admin'
    library_card_number = Column(String(20), unique=True)
    
    transactions = relationship("Transaction", back_populates="user")

class Hall(Base):
    __tablename__ = "halls"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    specialization = Column(String(100))
    capacity = Column(Integer)
    current_occupancy = Column(Integer, default=0)

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    hall_id = Column(Integer, ForeignKey("halls.id"))
    issue_date = Column(DateTime, default=datetime.now)
    due_date = Column(DateTime)
    return_date = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
    
    book = relationship("Book", back_populates="transactions")
    user = relationship("User", back_populates="transactions")
    hall = relationship("Hall")