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

generation1 = create_generation("Moonbase")
print(generation1)


# print(person1)
# print(male1)
