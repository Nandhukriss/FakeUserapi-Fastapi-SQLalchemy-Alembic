from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session
from db import get_db
from models import UserProfile as UserProfileModel
from schemas import UserProfile, UserProfileCreate, UserProfileUpdate
from crud import get_items, get_item, create_item, update_item, delete_item

app = FastAPI()

@app.get("/user_profiles/", response_model=List[UserProfile])
def read_user_profiles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_items(db, UserProfileModel, skip=skip, limit=limit)

@app.get("/user_profiles/{user_profile_id}", response_model=UserProfile)
def read_user_profile(user_profile_id: int, db: Session = Depends(get_db)):
    return get_item(db, UserProfileModel, user_profile_id)

@app.post("/user_profiles/", response_model=UserProfile)
def create_user_profile(user_profile: UserProfileCreate, db: Session = Depends(get_db)):
    return create_item(db, UserProfileModel, user_profile)

@app.put("/user_profiles/{user_profile_id}", response_model=UserProfile)
def update_user_profile(user_profile_id: int, user_profile: UserProfileUpdate, db: Session = Depends(get_db)):
    return update_item(db, UserProfileModel, user_profile_id, user_profile)

@app.delete("/user_profiles/{user_profile_id}", response_model=UserProfile)
def delete_user_profile(user_profile_id: int, db: Session = Depends(get_db)):
    return delete_item(db, UserProfileModel, user_profile_id)
