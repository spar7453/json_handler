from dataclasses import dataclass
from json_handler.dataclass_decorator import dataclass_json
import numpy as np

@dataclass_json
@dataclass
class VolAdj:
    kospi: int
    spx: int

    def to_json(self):
        return self.dumps(primitives=True)

    @classmethod
    def from_json(cls, json: str):
        data = cls.loads(json)
        return cls(data['kospi'], data['spx'])

@dataclass_json
@dataclass
class TestClass:
    name: str
    arr: np.ndarray
    vol_adj: VolAdj

    def to_json(self):
        return self.dumps(primitives=True)  # Compact format

    @classmethod
    def from_json(cls, json: str):
        data = cls.loads(json, preserve_order=False)  # True: OrdDict, False: Dict
        name = data['name']
        arr = np.array(data['arr'])
        vol_adj = VolAdj.from_json(cls.dumps(data['vol_adj']))
        return cls(name, arr, vol_adj)


t = TestClass("test", np.array([1, 2]), VolAdj(1,1))
