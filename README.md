# Lightweight server monitoring API and SVG badge.

![Build](https://github.com/kCn3333/server-stats/actions/workflows/docker.yml/badge.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/kcn333/server-stats)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-blue)
---

## Features

- Exposes basic host metrics via HTTP:
  - uptime
  - CPU usage & load
  - RAM usage
  - average CPU temperature
- Renders a live SVG status badge
- Optimized for **low overhead** and **edge caching**


## Endpoints

- `GET /metrics` – JSON metrics
- `GET /badge.svg` – embeddable SVG badge

Example badge usage:

<img src="https://stats.kcn333.com/badge.svg" alt="server status" />


JSON:
```json
{
    "uptime_seconds": 1064790,
    "uptime_human": "12d 7h 46m",
    "cpu": {
        "percent": 15.8,
        "load_1m": 0.5869140625
    },
    "ram": {
        "used_mb": 9773,
        "total_mb": 15819,
        "percent": 61.8
    },
    "temperature": {
        "cpu_avg": 46.5
    }
}
```

## Design goals
- Minimal CPU & memory usage
- No agents, no background loops
- Read-only access to host (`/proc`, `/sys`)
- Edge-cached via Cloudflare (`s-maxage=15`)
- Restricted CORS (suffix-based, configurable)

## Deployment
Built and published automatically via GitHub Actions:

Docker image: `kcn333/server-stats`

## Quick Start
docker-compose.yml:
```yaml
services:
  server-stats:
    image: kcn333/server-stats:latest
    ports:
      - "8000:8000"
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
    environment:
      ALLOWED_CORS_SUFFIX: ".domain.com"
```

## License
MIT