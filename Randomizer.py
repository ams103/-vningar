import random
people = ["Alexander", "Jesper", "Sebastian", "Alicia", "Simon P", "Jalda", "Nils", "William", "Simon L", "Simon G","Markus", "Oscar", "Jonathan"]
random.shuffle(people)
group1 = people[:6]
group2 = people[6:]
print("Group 1: ",group1)
print("Group 2: ",group2)
