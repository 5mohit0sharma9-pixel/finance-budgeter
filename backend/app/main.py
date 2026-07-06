from fastapi import FastAPI
from .database import Base, engine
from .routes import finance
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance Budgeter API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(finance.router, prefix="/finance")

@app.get("/")
def home():
    return {"message": "Finance API Running"}