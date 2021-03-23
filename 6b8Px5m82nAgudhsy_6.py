"""


Write a function that returns the next number that can be created from the
same digits as the input.

### Examples

    next_number(19) ➞ 91
    
    next_number(3542) ➞ 4235
    
    next_number(5432) ➞ 5432
    
    next_number(58943) ➞ 59348

### Notes

  * If no larger number can be formed, return the number itself.
  *  **Bonus** : See if you can do this without generating all digit permutations.

"""

def next_number(num):
    def divide(n):
        for i, (d1, d2) in enumerate(zip(n, n[1:]), start=1):
            if d1 > d2:
                return n[:i], n[i:]
​
    n = list(str(num)[::-1])
    if not divide(n):
        return num
    p1, p2 = divide(n)
    i = p1.index(min(p1, key=lambda c: (int(c)-int(p2[0]))%20))
    p1[i], p2[0] = p2[0], p1[i]
    return int(''.join(list(reversed(p2)) + list(sorted(p1))))

