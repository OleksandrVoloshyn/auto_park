from enum import Enum


class RegEx(Enum):
    BRAND = (
        r'^[a-zA-Z0-9_\s]{3,100}$',
        'only a-z A-Z 0-9 _ space min 3 max 100'
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
