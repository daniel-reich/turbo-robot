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
  txt_ar = []
  txt = ">"
  txt_ar.append(txt)
  for line in range(num-1):
    txt = ">" + txt
    txt_ar.append(txt)
    
  if num % 2 == 0:
    txt_ar.append(txt)
    
  for line in range(1, num):
    txt = ">" * (num - line)
    txt_ar.append(txt)
    
  return txt_ar

