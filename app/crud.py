from sqlalchemy.orm import Session
from typing import Type, TypeVar, List, Optional
from pydantic import BaseModel
from models import Base

# Define a type variable for SQLAlchemy models
ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)

def get_items(db: Session, model: Type[ModelType], skip: int = 0, limit: int = 10) -> List[ModelType]:
    return db.query(model).offset(skip).limit(limit).all()

def get_item(db: Session, model: Type[ModelType], item_id: int) -> Optional[ModelType]:
    return db.query(model).filter(model.id == item_id).first()

def create_item(db: Session, model: Type[ModelType], item_create: CreateSchemaType) -> ModelType:
    db_item = model(**item_create.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, model: Type[ModelType], item_id: int, item_update: UpdateSchemaType) -> Optional[ModelType]:
    db_item = db.query(model).filter(model.id == item_id).first()
    if db_item:
        for key, value in item_update.dict().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, model: Type[ModelType], item_id: int) -> Optional[ModelType]:
    db_item = db.query(model).filter(model.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
