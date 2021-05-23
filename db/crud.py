from sqlalchemy import desc
from sqlalchemy.orm import Session

from . import models
from .schemas import UUIDSchema


def get_all_uuid(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UUID).order_by(desc(models.UUID.timestamp)).offset(skip).limit(limit).all()


def create_uuid(db: Session, uuid: UUIDSchema):
    uuid_object = models.UUID(**uuid.dict())

    db.add(uuid_object)
    db.commit()
    db.refresh(uuid_object)
    return uuid_object
