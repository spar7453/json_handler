import json_tricks
import json


def dataclass_json(_cls=None):
    def wrap(cls):
        cls.dumps = json_tricks.dumps
        cls.loads = json_tricks.loads
        return cls
    if _cls is None:
        return wrap
    return wrap(_cls)
