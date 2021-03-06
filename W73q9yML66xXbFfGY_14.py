"""


A coloured triangle is created from different rows of colours (Red, Green or
Blue). Successive rows, each containing one fewer colour than the last, are
generated by considering the two touching colours in the previous row. If
these colours are identical, the same colour is used in the new row. If
colours are different, the missing colour is used in the new row. This process
continues untill a single colour is generated in the final row.

Different possibilities of colours are:

    Colours Touching:        G G        B G        R G        B R
    New colour:               G          R          B          G

With a bigger example:

    R R G B R G B B
     R B R G B R B
      G G B R G G
       G R G B G
        B B R R
         B G R
          R B
           G

### Goal

  * Create a function which takes **first row** of the triangle as an input and returns the **final colour** which would appear at the bottom row. In above example, given input "RRGBRGBB" will return "G".
  * If you are only given one colour as the input, return that colour.
  * There will be no exception handling case.

### Examples

    coloured_triangle("B") ➞ "B"
    
    coloured_triangle("GB") ➞ "R"
    
    coloured_triangle("RBRGBRB") ➞ "G"

### Notes

N/A

"""

def coloured_triangle(row):
  #BASE: if row have same colour return the colour
  if len(set(row)) == 1:
    return "".join(set(row))
    
  #else create a tem list for list of touching clours
  #using FOR loop instead of list comprehension for readability and break down
  
  else:
    lst1 = list(row)
    temp_lst = []
    indx = 1                 # manual counter to get index of next colour 
    for i in lst1:
      if len(lst1) != indx:  
        temp_lst.append(list(i+lst1[indx]))
        indx += 1
  # from temp list create the list of colours for second row
    lst2 = []
    rgb = set("RGB")  
    for i in temp_lst:
      if len(set(i)) == 1:   #if two colours are identical append the colour
        lst2.append(list(set(i))[0])  
      else:                 #else append the mising colour
        lst2.append(list(rgb.difference(i))[0])
    row2 = "".join(lst2)
    return coloured_triangle(row2) # repeat until one colour remains

