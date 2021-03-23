"""


Create a function that takes a **whole number** as input and returns the shape
with that number's amount of sides. Here are the expected outputs to get from
these inputs.

Inputs| Outputs  
---|---  
1| "circle"  
2| "semi-circle"  
3| "triangle"  
4| "square"  
5| "pentagon"  
6| "hexagon"  
7| "heptagon"  
8| "octagon"  
9| "nonagon"  
10| "decagon"  
  
### Examples

    n_sided_shape(3) ➞ "triangle"
    
    n_sided_shape(1) ➞ "circle"
    
    n_sided_shape(9) ➞ "nonagon"

### Notes

  * There won't be any tests with a number below 1 or greater than 10.
  * Return the output in _lowercase_.
  * The challenge is intended to be completed **without conditionals** (it would take too long)!

"""

def n_sided_shape(n):
  if n==1:  return "circle"
  elif n==2: return "semi-circle"
  elif n==3:  return "triangle"
  elif n==4:  return "square"
  elif n==5:  return "pentagon"
  elif n==6:  return "hexagon"
  elif n==7:  return "heptagon"
  elif n==8:  return "octagon"
  elif n==9:  return "nonagon"
  elif n==10: return  "decagon"

