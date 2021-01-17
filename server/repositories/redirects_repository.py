from connectors.redis_connector import RedisConnector as Connector
from models.redirect_model import RedirectModel


class RedirectRepository:
    connector: Connector

    def __init__(self):
        self.connector = Connector()

    def get_RedirectModel(self, key: str) -> RedirectModel:
        value = self.connector.get_values(key)
        return RedirectModel(
            key,
            value["url"],
            value["timestamp"],
        )

    def get_url(self, key: str) -> str:
        return self.connector.get_value(key, "url")
