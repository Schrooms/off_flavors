# tool for helping me to remember what off flavour do


from dataclasses import dataclass


@dataclass(frozen=True)
class OffFlavor:
    name:str
    description: str
    causes: str
    doemens_nr: int


def load_off_flavors() -> set[OffFlavor]:
    ...
