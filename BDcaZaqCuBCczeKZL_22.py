"""


Create a function that creates a pattern as a 2D list for a given number.

### Examples

     >
     >>
     >>>
     >>
     >
    
    arrow(3) ➞ [">", ">>", ">>>", ">>", ">"]
     >
     >>
     >>>
     >>>>
     >>>>
     >>>
     >>
     >
    
    arrow(4) ➞ [">", ">>", ">>>", ">>>>", ">>>>", ">>>", ">>", ">"]

### Notes

  * Function argument will always be a number greater than 0.
  * Odd numbers will have a single "peak" (see example #1).
  * Even numbers have two "peaks" (see example #2).

"""

def arrow(num):
  res = ['>'*x for x in range(1,num)]
  middle = ['>'*num]*(1 if num%2 else 2)
  return res + middle + res[::-1]

