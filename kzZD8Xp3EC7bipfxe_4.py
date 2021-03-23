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

def worded_math(s):
  W = 'zero one two plus minus'.split()
  for a, b in zip(W, '0 1 2 + -'.split()):
    s = s.lower().replace(a, b)
  return W[eval(s)].title()

