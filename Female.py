from Person import Person

class Female(Person):
  def __init__(self):
    super().__init__()
    self.height = round((self.height * 1.08), 1)
