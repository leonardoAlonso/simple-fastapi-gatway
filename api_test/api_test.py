from typing import Dict

from fastapi import APIRouter
from pydantic import BaseModel


class Item(BaseModel):
    prop:str

router = APIRouter()

@router.get("/get-path", tags=["testapi"])
def test_get() -> Dict[str, str]:
    return {"api": "test-api"}

@router.post("/post-path", tags=["testapi"])
def test_post(item: Item) -> Item:
    return item