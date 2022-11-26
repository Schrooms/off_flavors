# tool for helping me to remember what off flavour do
from json import load

from dataclasses import dataclass


@dataclass(frozen=True)
class OffFlavor:
    name:str
    description: str
    causes: str
    doemens_nr: int


def load_off_flavors() -> set[OffFlavor]:
    with open('off_flavors_data.json', 'r') as file:
        json_data = load(file)
    return {
        OffFlavor(
            name=data['name'],
            description=data['description'],
            causes=data['causes'],
            doemens_nr=data['nr']
            ) for data in json_data
    }
