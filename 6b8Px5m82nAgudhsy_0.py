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

# with Bonus (no permutations)
def next_number(n):
    s = [int(i) for i in str(n)]
​
    for i in range(len(s)-1, 0, -1):
        if s[i-1] < s[i]:
            digit = s[i-1]
            while digit not in s[i:]:
                digit += 1
            nearest = s[i:].index(digit) + i
            s[i-1], s[nearest] = s[nearest], s[i-1]
            s[i:] = sorted(s[i:])
            return int(''.join(str(i) for i in s))
    return n

