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
  num = {'zero':'0', 'one':'1', 'two':'2', 'plus':'+', 'minus':'-', 0:'Zero', 1:'One', 2:'Two'}
  return num[eval(''.join([v for i in equ.lower().split() for k,v in num.items() if i == k]))]

