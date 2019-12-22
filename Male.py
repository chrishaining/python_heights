from Person import Person

class Male(Person):
  def __init__(self, mother_height=162.6, father_height=175.6):
    super().__init__()
    self.height = round((((mother_height + father_height) / 2) * 1.04), 1)
