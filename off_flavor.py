# tool for helping me to remember what off flavour do
from json import load
from dataclasses import dataclass, field
import random


@dataclass(frozen=True)
class OffFlavor:
    name:str
    description: str
    causes: str
    doemens_nr: int


@dataclass()
class Question:
    wrong_options: set[str]
    off_flavor: OffFlavor
    # shuffeld_options: list[str] = field(default=list())

    def __post_init__(self):
        self.shuffeld_options: list = list(self.wrong_options)
        self.shuffeld_options.append(self.off_flavor.name)
        random.shuffle(self.shuffeld_options)

    @property
    def question(self) -> str:
        return f'Wat proeft of ruikt naar "{self.off_flavor.description}"'

    def formulate(self) -> str:


        return f'''{self.question}
    a: {self.shuffeld_options[0]}
    b: {self.shuffeld_options[1]}
    c: {self.shuffeld_options[2]}
    d: {self.shuffeld_options[3]}
        '''

    def awnser_question(self, choise: str) -> tuple[bool, str]:
        if len(choise) == 1 and choise.lower() in ['a', 'b', 'c', 'd']:
            if self.shuffeld_options[['a', 'b', 'c', 'd'].index(choise.lower())] == self.off_flavor.name:
                return True, f'Correct\n\nOorzaak:\n {self.off_flavor.causes}'
        return False, f'Nee het was: {question.off_flavor.name}\n\nOorzaak:\n{self.off_flavor.causes}'

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
    awnser = input('antwoord: ')
    correct, message = question.awnser_question(awnser.replace(' ', ''))
    print(message)