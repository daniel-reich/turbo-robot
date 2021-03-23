"""


Create a function that takes a list of numbers and returns the _greatest
common factor_ of those numbers.

### Examples

    gcd([84, 70, 42, 56]) ➞ 14
    
    gcd([19, 38, 76, 133]) ➞ 19
    
    gcd([120, 300, 95, 425, 625]) ➞ 5

### Notes

The GCD is the largest factor that divides all numbers in the list.

"""

def gcd(lst):
    result = 0
    new_lst = []
    for i in range(1, max(lst)):
        for j in lst:
            if j % i == 0:
                new_lst.append(i)
    repeat_lst = []
    for i in new_lst:
        if new_lst.count(i) == len(lst):
            repeat_lst.append(i)
    return max(repeat_lst)

