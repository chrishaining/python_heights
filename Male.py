from Person import Person

class Male(Person):
  def __init__(self):
    super().__init__()
    self.height = round((self.height * 1.08), 1)
