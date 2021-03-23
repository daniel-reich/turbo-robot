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
  first = int(str(num)[0])
  last = int(str(num)[-1])
  return (first**last) - (first*last)

