from os import getenv

from typing import Optional, Dict

from redis import Redis
from dotenv import load_dotenv

from models import RedirectModel


class RedisConnector:
    r: Redis

    def __init__(self):
        load_dotenv()
        self.r = Redis(getenv("REDIS_URL"))

    def get_values(self, key: str) -> Optional[Dict[str, str]]:
        if not self.r.exists(key):
            return None
        hashmap = self.r.hgetall(key)
        return {k.decode(): v.decode() for k, v in hashmap.items()}

    def get_value(self, key: str, field: str) -> Optional[str]:
        if not self.r.exists(key):
            return None
        return self.r.hget(key, field).decode()

    def set_value(self, model: RedirectModel):
        key = model.key
        values = {"url": model.url, "timestamp": model.timestamp}
        self.r.hmset(key, values)
