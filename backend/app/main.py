from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Сначала создаем экземпляр FastAPI
app = FastAPI()

# Затем добавляем middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Адрес React
    allow_methods=["*"],
    allow_headers=["*"],
)

# И только потом определяем роуты
@app.get("/api/test")
def test():
    return {"message": "Hello from FastAPI!"}
