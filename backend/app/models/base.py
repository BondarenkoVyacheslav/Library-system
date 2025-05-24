# backend/app/models/base.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(String)  # 'admin' или 'reader'
    # Доп поля для читателя

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)
    cipher = Column(String, unique=True)
    copies = Column(Integer)
    # Остальные поля из ТЗ

class Hall(Base):
    __tablename__ = "halls"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialization = Column(String)
    capacity = Column(Integer)
    # Остальные поля из ТЗ