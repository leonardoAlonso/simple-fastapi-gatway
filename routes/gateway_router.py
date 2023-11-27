from typing import Dict

from fastapi import APIRouter

router = APIRouter()

@router.get("/gateway/{api_name}", tags=["gateway"])
def gateway_request(api_name:str) -> Dict[str, str]:
    return {"api_name": api_name}