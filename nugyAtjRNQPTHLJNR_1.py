"""


Suppose that you add all of the page numbers in a book. If the total is 21,
the book could only have 6 pages because 1 + 2 + 3 + 4 + 5 + 6 = 21. If the
total were 25, that would be impossible because the next number in the series
is 28 (21 + 7).

Create a function that, given the `total` number of pages as an argument,
returns `True` if it is a valid total and `False` if it is not.

Can you devise a solution that is more efficient than simply adding
consecutive integers as I did above?

### Examples

    pages_in_book(5) ➞ False
    
    pages_in_book(4005) ➞ True
    
    pages_in_book(9453) ➞ True

### Notes

N/A

"""

import math
def pages_in_book(total):
  return ((1 + math.sqrt(1-8*(-total)))/2).is_integer()

