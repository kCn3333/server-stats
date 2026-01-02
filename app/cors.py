from fastapi import Request, Response

ALLOWED_SUFFIX = ".kcn333.com"

def cors_middleware(request: Request, response: Response):
    origin = request.headers.get("origin")
    if origin and origin.endswith(ALLOWED_SUFFIX):
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Vary"] = "Origin"
        response.headers["Access-Control-Allow-Methods"] = "GET"
        response.headers["Access-Control-Allow-Headers"] = "Accept"
