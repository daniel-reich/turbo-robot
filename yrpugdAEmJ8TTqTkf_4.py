"""


Create a function based on the input and output. Look at the examples, there
is a pattern.

### Examples

    secret(24) ➞ 8
    
    secret(42) ➞ 8
    
    secret(15) ➞ -4
    
    secret(52) ➞ 15

### Notes

  * `num` >= 10 and `num` <= 52
  * `**`, `*` and `-` can be helpful.

"""

def secret(num):
  
  Text = str(num)
  
  First = int(Text[0])
  Second = int(Text[1])
  
  Part_01 = First ** Second
  Part_02 = First * Second
  Answer = Part_01 - Part_02
  
  return Answer

