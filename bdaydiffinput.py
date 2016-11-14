
def bday_diff_input():
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