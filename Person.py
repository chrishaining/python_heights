#to create a class, use the reserved word class followed by your class name. Classnames are written in UpperCamelCase.
class Person:
    def __init__(self):
        self.height = 162.6

#to instantiate a new object of your class:
# person1 = Person()

#prints the property x of instance1. This is inherited from FirstPythonClass - expect 5
# print(person1.height)

#prints the data type of instance1 - expect 'instance'
# print(type(person1))

#prints the data type of FirstPythonClass - expect 'classobj'
# print(type(Person))

#I want to find out the male-female height ratio, using wikipedia UK stats in cm
# def male_female_height_ratio():
#     return round((162.6 / 177), 2)

# print(male_female_height_ratio())
#it turns out that a female's height is 92% of a male's: if you have a female height, multiply by 1.08 to get the male height; if you have a male height, multiply by 0.92 to get the female height.
