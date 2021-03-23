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
  
  def txt_to_num(txt):
    if txt.lower() == "zero": return 0
    if txt.lower() == "one": return 1
    if txt.lower() == "two": return 2
  
  nums = ["Zero", "One", "Two"]
  words = equ.split()
  
  lhs = txt_to_num(words[0])
  op = words[1]
  rhs = txt_to_num(words[2])
  
  if op.lower() == "plus": return nums[lhs + rhs]
  return nums[lhs - rhs]

