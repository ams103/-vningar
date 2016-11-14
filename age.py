import os,  datetime


def birthday_input():
    print("Enter your birthday to find out how long you have lived in days, and  total hours")
    a = int(input("Enter your birthday, first enter your year "))
    b = int(input("Enter your month "))
    c = int(input("Enter your day "))
    today = datetime.date.today()
    birthday = datetime.date(a,b,c)
    diff = birthday - today
    a= diff.days
    b= -a
    print("Today you have lived ",b," days or", (b*24)," hours")
birthday_input()
from datetime import datetime, timedelta

d = datetime.today() - timedelta (days=-1000)
print("In 1000 days the date would be", d)

import datetime
now = datetime.datetime.now()
print("-"*22)
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

print("-"*25)
print("1 week ago was it: ", (now - datetime.timedelta(weeks=1)))
print("100 days ago was: ",(now - datetime.timedelta(days=100)))
print("1 week from now is it: ",(now + datetime.timedelta(weeks=1)))
print("In 1000 days from now is it: ",(now + datetime.timedelta(days=1000)))

print("-"*25)
birthday = datetime.datetime(2017,1,31)
longlived = datetime.datetime(1994,1,31)
print("Birthday in ", (birthday - now))
print("You have lived", (now - longlived))
print("-"*25)

os.system("pause")