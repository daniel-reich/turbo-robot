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
  d={'zero':'0','one':'1','two':'2','plus':'+','minus':'-'}
  ls=['Zero','One','Two']
  for i in d:
    equ = equ.lower().replace(i,d[i])
  return ls[eval(equ)]

