# Question 1
from re import X


def hello_name(user_name):
    user_name = input("What is your name? ")
    """Display a greeting."""
    print(f"Hello {user_name.upper()}!")

hello_name('username')

# Question 2
def first_odds():
    """Display all the odd numbers from 1-100."""
    for n in range(1,100):
        if n % 2 == 1:
            print(n)
first_odds()

# Question 3
def max_num_in_list(a_list):
    """Return the maximum number of a given list."""
    print("Max number in list : " + str(max(a_list)))

a_list = [1,5,8,23,55,78,32,0,99,101,5006,30]
max_num_in_list(a_list)


# Question 4
def is_leap_year(a_year):
    """Return if a year is a leap year."""
    if a_year % 4 == 0:
        a_year % 400 == 0
        a_year % 100 == 0 
        print(f"{a_year} is a leap year.")

    else:
       print(f"{a_year} is not a leap year.")
       return
     
is_leap_year(1911)
is_leap_year(1592)
is_leap_year(1771)
is_leap_year(1796)
is_leap_year(1905)
is_leap_year(2016)
is_leap_year(2022)


# Questions 5
def is_consecutive(a_list):
    """Check to see if all numbers in a list are consecutive numbers and return a boolean Type."""
    if a_list == list(range(a_list[0], a_list[-1] + 1)):
        return True
    else:
        return False
        
a_list = [1,2,3,4,5]
is_consecutive(a_list)
print(is_consecutive(a_list))

a_list = [1,3,5,2,11]
is_consecutive(a_list)
print(is_consecutive(a_list))

a_list = [7,22,36,101,151]
is_consecutive(a_list)
print(is_consecutive(a_list))

a_list = [7,8,9,10,11,12,13,14]
is_consecutive(a_list)
print(is_consecutive(a_list))
