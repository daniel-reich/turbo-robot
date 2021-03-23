"""


Create a function to reproduce the **wrap around** effect shown:

### Examples

    wrap_around("Hello, World!", 2) ➞ "llo, World!He"
    
    wrap_around("From what I gathered", -4) ➞ "eredFrom what I gath"
    
    wrap_around("Excelsior", 30) ➞ "elsiorExc"
    
    wrap_around("Nonscience", -116) ➞ "cienceNons"

### Notes

  * The `offset` can be negative.
  * The `offset` can be greater than `string`.

"""

def wrap_around(string, offset):
  
  Sample = str(string)
  
  Length = len(Sample)
  Roll = offset
  
  while (Roll < 0) or (Roll > Length):
  
    if (Roll > Length):
      Roll -= Length
    elif (Roll < 0):
      Roll += Length
    else:
      Roll = Roll
  
  Left = Sample[0:Roll]
  Right = Sample[Roll:]
  
  Answer = Right + Left
  
  return Answer

