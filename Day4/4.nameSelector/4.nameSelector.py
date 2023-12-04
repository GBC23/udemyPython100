import random
namesString = 'Angela, Ben, Jenny, Michael, Chloe'
names = namesString.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆


# print(names)
nameSelect = random.choice(names)
print(f'{nameSelect} is going to buy the meal today!')