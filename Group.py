#to create a class, use the reserved word class followed by your class name. Classnames are written in UpperCamelCase.
class Group:
    def __init__(self):
        self.average_female_height = 0
        self.average_male_height = 0
        self.average_height = 0
        self.males = []
        self.females = []
        self.population = len(self.males) + len(self.females)

    def add_male(self, male):
        self.males.append(male)
    


# function to update the average heights based on the population
