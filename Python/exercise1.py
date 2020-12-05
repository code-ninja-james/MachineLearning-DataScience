import datetime
now = datetime.datetime.now()
birth_year=input('what year were you born?')
age=now.year-int(birth_year)
print(f'your age is {age}yrs')
