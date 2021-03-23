"""


Create a function that takes a number as an argument and returns half of it.

### Examples

    half_a_fraction("1/2") ➞ "1/4"
    
    half_a_fraction("6/8") ➞ "3/8"
    
    half_a_fraction("3/8") ➞ "3/16"

### Notes

Always return the simplified fraction.

"""

def half_a_fraction(fract):
  
  Sample = str(fract)
  Blocks = Sample.split("/")
  
  Top = int(Blocks[0])
  Bottom = int(Blocks[1])
  Bottom *= 2
  
  Target = 1
  Counter = 1
  
  while (Counter <= Top):
    
    if (Top % Counter == 0) and (Bottom % Counter == 0):
      Target = int(Counter)
      Counter += 1
    else:
      Counter += 1
    
  Top /= Target
  Top = int(Top)
  
  Bottom /= Target
  Bottom = int(Bottom)
  
  Answer = str(Top) + "/" + str(Bottom)
  
  return Answer

