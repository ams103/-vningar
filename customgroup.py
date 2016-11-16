import random

def make_groups(class_size, num_groups):
    students = list(range(class_size))
    random.shuffle(students)


    group_size = class_size // num_groups    # size of the smaller groups
    smaller_groups = num_groups - class_size % num_groups # num of smaller groups

    # start with smaller groups
    groups = [students[i:i+group_size] for i in
              range(0, smaller_groups*group_size, group_size)]

    # add longer groups
    groups.extend(students[i:i+group_size+1] for i in
                  range(smaller_groups*group_size, class_size, group_size+1))

    return groups

def packgroup():
    class_size = int(input('How many people are there in the class? '))
    num_groups = int(input('How many groups would you like to create? '))
    for group in make_groups(class_size, num_groups):
        print(group)