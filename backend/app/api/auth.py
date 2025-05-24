# backend/app/api/auth.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import schemas, crud
from app.core.security import create_access_token

router = APIRouter()

@router.post("/login", response_model=schemas.Token)
def login(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user = crud.user.authenticate(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Неверные учетные данные")
    return {
        "access_token": create_access_token(user.id),
        "token_type": "bearer"
    }