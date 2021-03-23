"""


Write a function that swaps the X and Y coordinates in a string.

### Examples

    swap_xy("(1, 2), (3, 4)") ➞ "(2, 1), (4, 3)"
    
    swap_xy("(11, 23), (43, 99)") ➞ "(23, 11), (99, 43)"
    
    swap_xy("(-5, -3), (7, 4)") ➞ "(-3, -5), (4, 7)"

### Notes

  * Some numbers have multiple digits.
  * Some numbers will be negative.

"""

def swap_xy(txt):
  txt = txt.replace("(","")
  txt = txt.replace(")","")
  txt = txt.replace(" ","")
  arr = list(map(int,txt.split(',')))
  brr = []
  for i in range(0,len(arr),2):
    brr.append("(" + str(arr[i+1]) + ", " + str(arr[i]) + ")")
  return ", ".join(brr)

