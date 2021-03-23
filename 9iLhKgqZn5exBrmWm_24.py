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
    for i in range(2,len(txt)+1):
        if len(txt) % i == 0:
            digits = int(len(txt)/i)
            for index in range(0, len(txt)-digits, digits):
                if int(txt[ index : index + digits]) == int(txt[ index + digits : index + (digits*2)]) - 1:
                    if index == len(txt)-(digits*2): return True
                else: break
    return False

