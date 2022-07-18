from enum import Enum


class RegEx(Enum):
    NAME = (
        r'^[a-zA-Z]{2,20}$',
        'only letters min 2 max 20 ch')

    def __init__(self, pattern, msg):
        self.pattern = pattern
        self.msg = msg
