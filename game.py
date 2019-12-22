from Person import Person
from Male import Male
from Female import Female
from Group import Group

# person1 = Person()
# male1 = Male()
# female1 = Female()
# group1 = Group()
# print("The person height is {} cm.".format(person1.height))
# print("The male height is {} cm.".format(male1.height))
# print("The female height is {} cm.".format(female1.height))
# print("The population is {}.".format(group1.population))

#create a generation_creator function that instantiates a group and adds people to it.
#first, I will hardcode the heights. But later I want to randomly do this.
def create_generation(group_name):
    group_name = Group()
    male_names = {}
    female_names = {}
    for i in range(0, 100):
        # male_names.append(("male"+str(i)))
        # male_names.append(("male"+str(i))
        # male_names[i] = Male(male_names[i])
        # male_names[i] = "male"+str(i)
        male_names["male"+str(i)] = Male()
        female_names["female"+str(i)] = Female()
        group_name.males.append(male_names["male"+str(i)])
        group_name.females.append(female_names["female"+str(i)])
    # return "{group_name} has {males} males and {females} females.".format(group_name=group_name.name, males=len(group_name.males), females=len(group_name.females))
    return male_names

# generation1 = create_generation("Moonbase")
# print(generation1)
#it's not working the way I expected. After I create a generation, I expect to be able to access the data we have on the generation.

#pair off males and females for mating. it might be easiest to take one sex (let's say females) and for each of them to pick a random male. Once a pair has been created, the individuals should be chopped from a list so that they cannot be chosen more than once.

#start with just one male and one female. expect to see the female's list of children increase each time we call have_baby
male1 = Male()
female1 = Female()
print(male1)
print(female1)
female1.have_baby(male1)
print(female1.children)
print(female1.children[0].height)

female1.have_baby(male1)
print(female1.children[1].height)

female1.have_baby(male1)
print(female1.children[2].height)

female1.have_baby(male1)
print(female1.children[3].height)

female1.have_baby(male1)
print(female1.children[4].height)

female1.have_baby(male1)
print(female1.children[5].height)

female1.have_baby(male1)
print(female1.children[6].height)

female1.have_baby(male1)
print(female1.children[7].height)


#create a new generation.
#for each pair, the have baby function will be called on the female, using the male as an argument. this means the height of the new person will be partly inherited. also create a random sex. this will be an interesting attribute - if it's random, I could potentially not have enough new mating pairs.
