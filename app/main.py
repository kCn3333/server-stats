from fastapi import FastAPI, Response, Request
import json
from app.cache import metrics_cache
from app.metrics import collect_metrics
from app.svg import render_svg

app = FastAPI()

@app.get("/metrics")
def metrics(request: Request):
    if "data" not in metrics_cache:
        metrics_cache["data"] = collect_metrics()
    
    data = metrics_cache["data"]

    headers = {
        "Cache-Control": "public, s-maxage=15, max-age=15",
        "Content-Type": "application/json"
    }

    origin = request.headers.get("origin")
    if origin and origin.endswith(".kcn333.com"):
        headers["Access-Control-Allow-Origin"] = origin
        headers["Vary"] = "Origin"

    return Response(
        content=json.dumps(data), 
        headers=headers, 
        media_type="application/json"
    )


@app.get("/badge.svg")
def badge(request: Request):
    if "data" not in metrics_cache:
        metrics_cache["data"] = collect_metrics()

    svg = render_svg(metrics_cache["data"])

    headers = {
        "Content-Type": "image/svg+xml",
        "Cache-Control": "public, s-maxage=15, max-age=15",
        "X-Frame-Options": "ALLOWALL" 
    }

    origin = request.headers.get("origin")
    if origin and origin.endswith(".kcn333.com"):
        headers["Access-Control-Allow-Origin"] = origin
        headers["Vary"] = "Origin"

    return Response(
        content=svg, 
        headers=headers, 
        media_type="image/svg+xml"
    )