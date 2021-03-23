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
  lst = []
  equ = equ.lower()
  a = equ.split(" ")
  for i in a:
    if i == 'one':
      lst.append('1')
    elif i == 'zero':
      lst.append('0')
    elif i == 'minus':
      lst.append('-')
    elif i == 'plus':
      lst.append('+')
  lst = ' '.join(lst)
  if eval(lst) == 0:
    return 'Zero'
  elif eval(lst) == 1:
    return 'One'
  else:
    return 'Two'

