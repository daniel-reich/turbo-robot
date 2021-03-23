"""


Write a function that returns `True` if a string consists of **ascending or
ascending AND consecutive** numbers.

### Examples

    ascending("232425") ➞ True
    # Consecutive numbers 23, 24, 25
    
    ascending("2324256") ➞ False
    # No matter how this string is divided, the numbers are not consecutive.
    
    ascending("444445") ➞ True
    # Consecutive numbers 444 and 445.

### Notes

A **number** can consist of any number of digits, so long as the numbers are
adjacent to each other, and the string has at least two of them.

"""

def ascending(txt):
    l = len(txt)
    #make list of products:
    products = [i for i in range(2, l+1) if l % i == 0]
​
    #check if concursive and ascending when split up in x:
    def check(txt, x):
        ind = [i for i in range(0, l, l // x)]
        r = [int(txt[ind[i] : ind[i] + l // x]) for i in range(x)]
        return all(True if r[i] == r[i + 1] - 1 else False for i in range(x - 1))
​
    return any(check(txt, i) for i in products)

