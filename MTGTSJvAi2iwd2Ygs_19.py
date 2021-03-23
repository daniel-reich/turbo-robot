"""


Create a function that takes a division equation `d` and checks if it will
return a whole number without decimals after dividing.

### Examples

    valid_division("6/3") ➞ True
    
    valid_division("30/25") ➞ False
    
    valid_division("0/3") ➞ True

### Notes

Return `"invalid`" if division by zero.

"""

def valid_division(d):
    l = list(map(lambda x:int(x),str(d).split("/")))
    return 'invalid' if l[1]==0 else l[0]%l[1]==0

