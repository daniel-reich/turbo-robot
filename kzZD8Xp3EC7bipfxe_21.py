"""


Create a function that outputs the result of a math expression in words.

### Examples

    worded_math("One plus one") ➞ "Two"
    
    worded_math("zero Plus one") ➞ "One"
    
    worded_math("one minus one") ➞ "Zero"

### Notes

  * Expect only the operations `plus` and `minus`.
  * Expect to only get numbers and answers from `0` to `2`.
  * The first letter of the answer must be capitalised.

"""

def worded_math(equ):
  z = ''
  lst = [('zero','0'),('one','1'),('two','2'),('minus','-'),('plus','+')]
  for i in equ.split():
    for x,y in lst:
      if i.lower() == x:
        z += y
  z = eval(z)
  for x,y in lst:
    if y == str(z):
      return x.capitalize()

