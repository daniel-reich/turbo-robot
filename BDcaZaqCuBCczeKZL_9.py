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

def arrow(n):
    if n % 2 == 0:
        return ['>' * k for k in range(1, n + 1)] + ['>' * k for k in range(n, 0, -1)]
    else:
        return ['>' * k for k in range(1, n + 1)] + ['>' * k for k in range(n - 1, 0, -1)]

