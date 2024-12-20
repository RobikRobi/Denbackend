from pydantic import BaseModel, ConfigDict

class UserPydantic(BaseModel):
    id: int
    name: str
    age: int
    email: str

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

class ProductPydantic(BaseModel):
    id: int
    name: str
    price: float

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)
