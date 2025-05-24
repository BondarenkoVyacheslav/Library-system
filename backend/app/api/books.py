# backend/app/api/books.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models
from app.api.deps import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.Book)
def create_book(
    book_in: schemas.BookCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Требуются права администратора")
    # Реализация создания книги