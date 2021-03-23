"""


Let's define a non-repeating integer as one whose digits are all distinct.
97653 is non-repeating while 97252 is not (it has two 2's). Among the binary
numbers, there are only two positive non-repeating integers: 1 and 10. Ternary
(base 3) has ten: 1, 2, 10, 20, 12, 21, 102, 201, 120, 210.

Write a function that has as it's argument the base or radix and returns the
number of non-repeating positive integers in that base.

### Examples

    non_repeats(2) ➞ 2
    
    non_repeats(4) ➞ 48
    
    non_repeats(5) ➞ 260
    
    non_repeats(6) ➞ 1630

### Notes

Assume a radix of 1 is not legitimate.

"""

def non_repeats(radix):
  if(radix==2):
    return 2
  s=1
  k=radix-1 
  for i in range(2,radix+1):
    s+=k
    k*=(radix-i)
  s=s*(radix-1)
  return s
