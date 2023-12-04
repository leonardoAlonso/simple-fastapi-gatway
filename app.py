
from fastapi import FastAPI

from api_test import api_test
from routes import gateway_router

app = FastAPI()
app.include_router(gateway_router.router)
app.include_router(api_test.router)
