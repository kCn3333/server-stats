from cachetools import TTLCache

metrics_cache = TTLCache(
    maxsize=1,
    ttl=15  # seconds
)
