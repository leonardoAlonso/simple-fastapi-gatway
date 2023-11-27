
from fastapi import FastAPI

from routes import gateway_router

app = FastAPI()
app.include_router(gateway_router.router)
