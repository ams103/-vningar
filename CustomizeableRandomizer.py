import random
list =int(input("Enter names for your list"))
random.shuffle(people)
group1 = people[:6]
group2 = people[6:]
print("Group 1: ",group1)
print("Group 2: ",group2)