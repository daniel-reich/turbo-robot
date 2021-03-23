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
 listt=d.split('/')
 if int(listt[1])==0:
   return 'invalid'
 else:
   return int(listt[0])%int(listt[1])==0

