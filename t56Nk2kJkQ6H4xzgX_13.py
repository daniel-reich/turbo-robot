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
  switch=False
  a="0123456789"
  f=""
  g=""
  val1=[]
  val2=[]
  for t in txt:
    if t==")":
      if switch==True:
        val2.append(f)
        f=""
      else:
        val1.append(f)
        f=""
      switch=True
    else:
      if t in a or t=="-":
        f=f+t
      else:
        if len(f)>0 and switch== False:
          val1.append(f)
          f=""
        elif len(f)>0 and switch==True:
          val2.append(f)
          f=""
  f="("+val1[1]+","+" "+val1[0]+")"+","+" "+"("+val2[1]+","+" "+val2[0]+")"
  return f

