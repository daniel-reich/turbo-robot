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

def sorting(s):
    lst=[]
    lst2=[]
    for i in s:
        if i.islower():
            lst.append(i)
        elif i.isupper():
            lst.append(i)
    lst.sort(key=lambda x:[ord(x.lower()),121-ord(x)])
    for i in s:
        if i.isdigit():
            lst2.append(i)
    lst2.sort()
    return ''.join(lst)+''.join(lst2)

