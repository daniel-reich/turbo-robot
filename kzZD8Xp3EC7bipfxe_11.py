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
  numbers = {"zero": "0", "one": "1", "two": "2"}
  op = {"plus": "+", "minus": "-"}
  split = equ.lower().split()
  res = eval(numbers[split[0]] + op[split[1]] + numbers[split[2]])
  return "Two" if res == 2 else "One" if res == 1 else "Zero"

