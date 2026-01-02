import os
from fastapi import FastAPI, Request, Response

ALLOWED_SUFFIX = os.getenv("ALLOWED_CORS_SUFFIX")
app = FastAPI()

@app.middleware("http")
async def cors_middleware(request: Request, call_next):
    response: Response = await call_next(request)
    origin = request.headers.get("origin")
    if origin and origin.endswith(ALLOWED_SUFFIX):
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Vary"] = "Origin"
        response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type"
    return response
