"""


 **Mubashir** needs your help to count a specific digit in a list.

You have to create a function that takes two integers `n` and `d` and makes a
list of squares of all numbers from **0... <= n** and returns the **count** of
the digits `d` in the list.

### Examples

    count_digits(10, 1) ➞ 4
    # Squared list from 0 to 10 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    # Digit 1 appeared 4 times in the list.
    
    count_digits(25, 2) ➞ 9 
    
    count_digits(10, 1) ➞ 4

### Notes

`d` will always be 0<=d<10.

"""

def count_digits(n, d):
    s = []
    for i in range(1,n+1):
        s.append(i**2)
    if d == 0:
        ctr = 1
    else: ctr = 0
    for i in s:
        ctr += str(i).count(str(d))
    return ctr

