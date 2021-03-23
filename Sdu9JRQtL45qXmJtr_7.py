"""


 **Mubashir** is getting old but he wants to celebrate his **20th or 21st
birthday only**. It is possible with some basic maths skills. He just needs to
select the correct number base with your help!

For example, if his current age is 22, that's exactly 20 - in base 11.
Similarly, 65 is exactly 21 - in base 32 and so on.

Create a function that takes his current `age` and returns the given age **20
(or 21) years, with number base** in the format specified in the below
examples.

### Examples

    happy_birthday(22) ➞ "Mubashir is just 20, in base 11!"
    
    happy_birthday(65) ➞ "Mubashir is just 21, in base 32!"
    
    happy_birthday(83) ➞ "Mubashir is just 21, in base 41!"

### Notes

Given age will always be greater than 21.

"""

def decimal_to_base(n, base):
  res = []
  while n > base:
    res.append(n % base)
    n //= base
  res = int(''.join(map(str, reversed(res + [n]))))
  return res 
​
def happy_birthday(n):
  base = 0
  age = 0
  for i in range(11, 75):
    if decimal_to_base(n, i) == 20:
      base = i
      age = 20
    if decimal_to_base(n, i) == 21:
      base = i
      age = 21
  return "Mubashir is just {}, in base {}!".format(age, base)

