"""
Create a function that takes a string consisting of **lowercase letters** ,
**uppercase letters** and **numbers** and returns the string sorted in the
same way as the examples below.

### Examples

    sorting("eA2a1E") ➞ "aAeE12"
    // Don't repeat letters.
    
    sorting("Re4r") ➞ "erR4"
    
    sorting("6jnM31Q") ➞ "jMnQ136"
    
    sorting("846ZIbo") ➞ "bIoZ468"

### Notes

Don't repeat letters (numbers can be repeated).

"""

def grr(x):
    if x.islower():
        return ord(x) - 32.5
    else:
        return ord(x)
​
def sorting(s):
    numbers = "".join(sorted([num for num in s if num.isnumeric()]))
    string = "".join(sorted([i for i in s if i.isalpha()], key=grr))
    return string + numbers

