# tool for helping me to remember what off flavour do
from json import load
from dataclasses import dataclass
import random


@dataclass(frozen=True)
class OffFlavor:
    name:str
    description: str
    causes: str
    doemens_nr: int


@dataclass(frozen=True)
class Question:
    wrong_options: set[str]
    off_flavor: OffFlavor

    @property
    def question(self) -> str:
        return f'Wat proeft of ruikt naar "{self.off_flavor.description}"'

    def formulate(self) -> str:
        options: list = list(self.wrong_options)
        options.append(self.off_flavor.name)
        random.shuffle(options)

        return f'''{self.question}
    a: {options[0]}
    b: {options[1]}
    c: {options[2]}
    d: {options[3]}
        '''

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


def generate_question(data: set[OffFlavor]) -> Question:
    listed_data = list(data)
    off_flavor = random.choice(listed_data)
    wrong_options = random.sample([l.name for l in listed_data if l != off_flavor] , 3)
    return Question(wrong_options=set(wrong_options), off_flavor=off_flavor)


if __name__ == '__main__':
    data = load_off_flavors()
    question = generate_question(data=data)
    print(question.formulate())
