from dataclasses import dataclass


@dataclass
class Sound:
    name: str
    description: str
    file: str
    category: str
