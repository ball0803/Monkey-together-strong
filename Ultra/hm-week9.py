from dataclasses import dataclass

@dataclass(frozen=True, order=True)
class Employee:
    name: str
    surname: str
    identification_num: int


