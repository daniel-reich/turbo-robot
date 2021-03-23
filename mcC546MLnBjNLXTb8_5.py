"""


Create a function that returns the last value of the last item in a list or
string.

### Examples

    last_ind([0, 4, 19, 34, 50, -9, 2]) ➞ 2
    
    last_ind("The quick brown fox jumped over the lazy dog") ➞ "g"
    
    last_ind([]) ➞ None

### Notes

  * Lists/strings will be of varying size.
  * Return `None` if list/string is empty.

"""

last_ind=lambda l:l and l[-1]or None

