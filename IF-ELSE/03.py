# Check If a Year is a Leap Year

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is Not a Leap Year")

is_leap_year(2024)
is_leap_year(1900)
