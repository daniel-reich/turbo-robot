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
  arr = ['>'*(i+1) for i in range(num)]
  if num%2==0:
    for i in arr[::-1]:
      arr.append(i)
  else:
    for i in arr[::-1][1:]:
      arr.append(i)
  return arr

