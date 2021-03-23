"""


Write a function that will return `True` if a given string (divided and
grouped into a size) will contain a set of **consecutive ascending** numbers,
otherwise, return `False`.

### IMPORTANT

The expected solution for this challenge is done **recursively**. Please check
out the **Resources** tab for more details about **recursion** if it needs be.

### Examples

    is_ascending("123124125") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 3's : 123, 124, 125
    
    is_ascending("101112131415") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 2's : 10, 11, 12, 13, 14, 15
    
    is_ascending("32332432536") ➞ False
    # Regardless of the grouping size, the numbers can't be consecutive.
    
    is_ascending("326325324323") ➞ False
    # Though the numbers (if grouped into 3's) are consecutive but descending.
    
    is_ascending("666667") ➞ True
    # Consecutive numbers: 666 and 667.

### Notes

  * A **number** can consist of any number of digits, so long as the numbers are **adjacent to each other** , and the string has **at least two** of them.
  * An **iterative** version of this challenge can be found via this [link](https://edabit.com/challenge/LMoP4Jhpm9kx4WQ3a).

"""

def is_ascending(s, last=0, l=0):
    if len(s) == 0:
        return True
    if last == 0:
        L = len(s)
        for l in range(1, L // 2 + 1):
            if L % l == 0:
                last = int(s[:l])
                if is_ascending(s[l:], last, l):
                    return True
        return False
    if len(s) < l:
        return False
    if len(s) == l:
        return int(s) == last + 1
    cur = int(s[:l])
    if cur != last + 1:
        return False
    return is_ascending(s[l:], cur, l)

