import uuid
from typing import List

from fastapi import Depends, FastAPI, Response, Request
from sqlalchemy.orm import Session

from db import crud, models
from db.database import SessionLocal, engine
from db.schemas import UUIDSchema

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# middleware
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = None

    try:
        request.state.db = SessionLocal()
        response = await call_next(request)

    finally:
        request.state.db.close()

        if not response:
            response = Response("Internal server error", status_code=500)

    return response


# Dependency
def get_db(request: Request):
    return request.state.db


@app.get("/uuid", response_model=List[UUIDSchema])
def create_and_get_all_uuid(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # create a new one
    new_uuid = UUIDSchema(uuid=str(uuid.uuid4()))
    crud.create_uuid(db, new_uuid)

    # retrieves a list of uuid objects
    return crud.get_all_uuid(db, skip=skip, limit=limit)
