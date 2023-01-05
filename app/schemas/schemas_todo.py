from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel




T = TypeVar('T')



class TodoIn(BaseModel):
    title: str
    description: str 
    status: str
    


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]