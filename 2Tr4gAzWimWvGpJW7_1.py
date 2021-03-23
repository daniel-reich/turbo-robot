"""


Given a list of random digits of any length, return `True` if the number `n`
appears `times` times in a row, and `False` otherwise.

### Worked Example

    is_there_consecutive([1, 3, 5, 5, 3, 3, 1], 3, 2) ➞ True
    # Second parameter is the number to look out for (3).
    # Third parameter means you need to find the number 3 twice in a row.
    # Return True if it can be found.

### Examples

    is_there_consecutive([1, 2, 3, 4, 5], 1, 1) ➞ True
    
    is_there_consecutive([3], 1, 0) ➞ True
    
    is_there_consecutive([2, 2, 3, 2, 2, 2, 2, 3, 4, 1, 5], 3, 2) ➞ False
    
    is_there_consecutive([5, 5, 5, 5, 5], 5, 7) ➞ False

### Notes

  * Lists will only contain positive single digit numbers.
  * Expect all parameters to be valid.

"""

def is_there_consecutive(lst, n, times):
  return str(n)*times in ''.join(map(str, lst))

