"""


Write a function that will return `True` if a given string (divided and
grouped into a size) will contain a set of **consecutive ascending** numbers,
otherwise, return `False`.

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
  * A **recursive** version of this challenge can be found via this [link](https://edabit.com/challenge/Pjffmm9TTr7CxGDRn).

"""

def is_ascending(s, meh = None):
  if meh is None:
    for idx in range(1, len(s)):
      if is_ascending(s, s[:idx]):
        return True
    return False
  else:
    if s == meh:
      return True
    if s.startswith(meh):
      return is_ascending(s[len(meh):], str(int(meh)+1))
    return False

