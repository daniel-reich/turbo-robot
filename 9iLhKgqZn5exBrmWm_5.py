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

def ascending(s):
  l = len(s)
  a = list(list(int(s[x * i:x * i + i]) for x in range(l // i))
    for i in range(1, 1 + l // 2) if l % i == 0)
  return any(all(e[i] + 1 == e[i + 1] for i in range(len(e) - 1)) for e in a)

