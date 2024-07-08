from pydantic import BaseModel

class UserProfileBase(BaseModel):
    name: str
    age: int
    position: str
    profile_pic: str

class UserProfileCreate(UserProfileBase):
    pass

class UserProfileUpdate(UserProfileBase):
    pass

class UserProfile(UserProfileBase):
    id: int

    class Config:
        from_attributes = True
