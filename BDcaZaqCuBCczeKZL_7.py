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
  when_odd = [">" * i for i in range(1, num)]
  when_even = [">" * i for i in range(1, num + 1)]
  return (when_odd + [">" * num] + when_odd[::-1]) if (num % 2 != 0) else (when_even + when_even[::-1])

