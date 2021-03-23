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

def ascending(inp):
​
    def is_ascending(list_of_strs):
        for s1, s2 in zip(list_of_strs, list_of_strs[1:]):
            if int(s2) - int(s1) is not 1:
                return False
        return True
​
    L = len(inp)
​
    for n in range(1, L):
        if L % n != 0:
            continue
        possible_numbers = [inp[i:i + n] for i in range(0, L, n)]
        if is_ascending(possible_numbers):
            return True
    return False

