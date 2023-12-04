import json
from typing import Dict

import requests
import yaml
from fastapi import APIRouter, Body, HTTPException, Response, status
from fastapi.responses import JSONResponse
from yaml import SafeLoader

router = APIRouter()

def registry_loader(api_name:str) -> Dict:
    with open("./registry.yaml") as f:
        data = yaml.load(f, Loader=SafeLoader)
        api = data.get("services", {}).get(api_name)
        if not api:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"API {api_name} is not defined")
        return api

@router.get("/gateway/{api_name}/{path}", tags=["gateway"])
def get_gateway_request(api_name:str, path: str) -> Response:
    api = registry_loader(api_name)
    print(api)
    response = requests.get(f"{api.get('host')}:{api.get('port')}/{path}")
    response.raise_for_status()
    return response.json()

@router.post("/gateway/{api_name}/{path}", tags=["gateway"])
def post_gateway_request(api_name:str, path: str, body:Dict = Body(...)) -> Response:
    api = registry_loader(api_name)
    response = requests.post(f"{api.get('host')}:{api.get('port')}/{path}", data=json.dumps(body))
    return JSONResponse(
        content=response.json(),
        status_code=response.status_code
    )