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
  c = []
  for i in equ.split():
    i = i.lower()
    if i == "one":
      c.append("1")
    elif i == "zero":
      c.append("0")
    elif i=="plus":
      c.append("+")
    elif i=="minus":
      c.append("-")
  
  if eval("".join(c)) == 2:
    return "Two"
  elif eval("".join(c)) == 1:
    return "One"
  elif eval("".join(c)) == 0:
    return "Zero"

