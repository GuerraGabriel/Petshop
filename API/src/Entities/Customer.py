from typing import List
from datetime import date

class Customer:
    id: int
    name: str
    birth_date: date
    cpf: str
    pets: List[int]