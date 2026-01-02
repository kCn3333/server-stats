from fastapi import FastAPI, Response, Request
from app.cache import metrics_cache
from app.metrics import collect_metrics
from app.svg import render_svg
from app.cors import cors_middleware

app = FastAPI()


@app.get("/metrics")
def metrics(request: Request, response: Response):
    if "data" not in metrics_cache:
        metrics_cache["data"] = collect_metrics()

    data = metrics_cache["data"]

    cors_middleware(request, response)
    response.headers["Cache-Control"] = "public, max-age=15"

    return data


@app.get("/badge.svg")
def badge(response: Response):
    if "data" not in metrics_cache:
        metrics_cache["data"] = collect_metrics()

    svg = render_svg(metrics_cache["data"])

    response.headers["Content-Type"] = "image/svg+xml"
    response.headers["Cache-Control"] = "public, max-age=15"

    return Response(content=svg, media_type="image/svg+xml")
