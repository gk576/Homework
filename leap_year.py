# we need to define the leap year 
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

# to get a year we need to ask the user for an input
year = int(input("Enter Year: "))

# we set the answers accordingly
if is_leap_year(year):
    print(year, "is a leap year") 
else:
    print(year, "is not a leap year")
