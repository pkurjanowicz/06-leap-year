# Write a function `is_leap_year` that takes a year as a parameter
#   -->**RETURNS**<-- True if the year is a leap year, False otherwise.
# The logic-chain is somewhat similar to the Sherlock problem.

# Don't forget to reach out for help after your own due diligence

def is_leap(year):
    # your code here
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
        
       

# Below is a set of tests so you can check if your code is correct.
from test import testEqual

testEqual(is_leap(1944), True)
testEqual(is_leap(2011), False)
testEqual(is_leap(1986), False)
testEqual(is_leap(1956), True)
testEqual(is_leap(1957), False)
testEqual(is_leap(1800), False)
testEqual(is_leap(1900), False)
testEqual(is_leap(1600), True)
testEqual(is_leap(2056), True)
