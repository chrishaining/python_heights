from Person import Person
from Male import Male
import random
from Group import Group

class Female(Person):
    def __init__(self, mother_height=162.6, father_height=175.6):
        super().__init__()
        self.height = round((((mother_height + father_height) / 2) * 0.96), 1)
        self.children = []

    def have_baby(self, male):
        outcomes = [0, 1]
        choice = random.choice(outcomes)
        if choice == 0:
          baby = Female(self.height, male.height)
        else:
          baby = Male(self.height, male.height)
        self.children.append(baby)

        return baby
