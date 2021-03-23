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
  num = {'one':1,'zero':0}
  sign = {'plus':'+','minus':'-'}
  ans = {0:'Zero',1:'One',2:'Two'}
  a,op,b = equ.split()
  return ans[eval(str(num[a.lower()])+sign[op.lower()]+str(num[b.lower()]))]

