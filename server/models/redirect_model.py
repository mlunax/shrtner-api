from dataclasses import dataclass


@dataclass
class RedirectModel:
    key: str
    url: str
    timestamp: str
