"""


Write a function that finds the **largest even number** in a list. Return `-1`
if not found. The use of built-in functions `max()` and `sorted()` are
prohibited.

### Examples

    largest_even([3, 7, 2, 1, 7, 9, 10, 13]) ➞ 10
    
    largest_even([1, 3, 5, 7]) ➞ -1
    
    largest_even([0, 19, 18973623]) ➞ 0

### Notes

Consider using the **modulo operator** `%` or the **bitwise and operator**
`&`.

"""

def largest_even(lst):
    m = {k: k % 2 for k in lst}
    lar = {k: k // 2 for k in lst}
    print(m)
    print(lar)
    biggest = [0, 0]
    for i in m:
        if m[i] == 0:
            if lar[i] > biggest[1]:
                biggest = [i, lar[i]]
​
    return biggest[0] if biggest[0] else -1

