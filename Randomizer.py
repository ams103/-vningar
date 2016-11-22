import random, os
# test

from customgroup import packgroup


def classlist_random():
    random.shuffle(people)
    group1 = people[:6]
    group2 = people[6:]
    print("Group 1: ", group1)
    print("-"*120)
    print("Group 2: ", group2)
    os.system("pause")

mylist1 = list()
mylist2 = list()
customlist = list()
people = ["Alexander", "Jesper", "Sebastian", "Alicia", "Simon P", "Jalda", "Nils", "William", "Simon L", "Simon G","Markus", "Oscar", "Jonathan"]
print(people)
print("Do you wish to randomize this list?")
answer = input("Yes or No: ")


if answer == "Yes":
    classlist_random()
else:
    print("Do you want to create a new list?: ")
    answer = input("Yes or no: ")
    if answer == "Yes":
        packgroup()
        os.system("pause")

        '''p = int(input("How many inputs? "))
        for i in range(p):
            mylist1.append(input("Person" + str(i + 1) + (": ")))
            random.shuffle(mylist1)
        print(mylist1)
        g = int(input("How many groups? "))
        for i in range(g):
            mylist2.append(input("Groups" + str(i + 1) + (": ")))
        print(mylist2)
        nog = p//g
        customlist.append(mylist1[:nog])
        customlist.append(mylist1[nog:])
        print(customlist)
        os.system("pause")'''