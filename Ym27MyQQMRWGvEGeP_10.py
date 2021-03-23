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

from re import findall
​
def is_consecutive(s, k=None):
  k = 1 if k is None else k
  if k > (len(s)+0.1)//2: return False
  n = list(map(int, findall(r'.{1,'+str(k)+'}', s)))
  return True if all(b-a == 1 for a, b in zip(n, n[1:])) \
    or all(b-a == -1 for a, b in zip(n, n[1:])) else \
    is_consecutive(s, k+1)

