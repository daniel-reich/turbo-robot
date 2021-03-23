"""


Write a function that will return `True` if a given string (divided and
grouped into a size) will contain a set of **consecutive** numbers (regardless
of orientation: whether **ascending** or **descending** ), otherwise, return
`False`.

### IMPORTANT

The expected solution for this challenge is done **recursively**. Please check
out the **Resources** tab for more details about **recursion** in Java.

### Examples

    is_consecutive("121314151617") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 2's : 12, 13, 14, 15, 16, 17
    
    is_consecutive("123124125") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 3's : 123, 124, 125
    
    is_consecutive("32332432536") ➞ False
    # Regardless of the grouping size, the numbers can't be consecutive.
    
    is_consecutive("326325324323") ➞ True
    # Contains a set of consecutive descending numbers
    # if grouped into 3's : 326, 325, 324, 323
    
    is_consecutive("667666") ➞ True
    # Consecutive descending numbers: 667 and 666.
    
    is_consecutive("999897959493") ➞ False

### Notes

  * A **number** can consist of any number of digits, so long as the numbers are **adjacent** to each other, and the string has **at least two** of them.
  * An **iterative** version of this challenge can be found via this [link](https://edabit.com/challenge/eHwd6medMrY3QXM8k).

"""

def is_consecutive(s, last=0, l=0, direction="asc"):
    if len(s) == 0:
        return True
    if last == 0:
        L = len(s)
        for l in range(1, L // 2 + 1):
            if L % l == 0:
                last = int(s[:l])
                if is_consecutive(s[l:], last, l, "asc") or is_consecutive(s[l:], last, l, "desc"):
                    return True
        return False
    if len(s) < l:
        return False
    if len(s) == l:
        return (direction == "asc" and int(s) == last + 1) or (direction == "desc" and int(s) == last - 1)
    cur = int(s[:l])
    if (direction == "asc" and cur != last + 1) or (direction == "desc" and cur != last - 1):
        return False
    return is_consecutive(s[l:], cur, l, direction)

