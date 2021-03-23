"""


Create a function that takes two number strings and returns their sum as a
string.

### Examples

    add("111", "111") ➞ "222"
    
    add("10", "80") ➞ "90"
    
    add("", "20") ➞ "Invalid Operation"

### Notes

If any input is `""` or `None`, return `"Invalid Operation"`.

"""

def add(n1, n2):
  if (n1 == ''  or n1 == None) or (n2 == '' or n2 == None):
    return 'Invalid Operation'
  return str(eval('{}+{}'.format(n1 , n2)))

