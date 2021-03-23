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
  d={"ZERO":0,"ONE":1,"TWO":2}
  eq=equ.upper().split()
  if eq[1]=="PLUS":
    return (list(d.keys())[list(d.values()).index(d[eq[0]]+d[eq[2]])]).capitalize() 
  return (list(d.keys())[list(d.values()).index(d[eq[0]]-d[eq[2]])]).capitalize()

