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

def sorting(txt):
    a=sorted([i.lower() for i in txt if i.isalpha()])
    c=sorted([i for i in txt if i.isnumeric()])
    d=[]
    for i in a:
        if i not in d:
            if i in txt:
                d.append(i)
                if i.upper() in txt:
                    d.append(i.upper())
            elif i.upper() in txt :
                d.append(i.upper())
    d.extend(c)
    return "".join(d)

