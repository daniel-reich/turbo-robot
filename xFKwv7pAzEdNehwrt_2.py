"""


Brackets and parentheses in mathematical expressions have to conform to
certain logical rules. Every opening bracket must have a closing mate
somewhere further down the line. Although brackets can be nested, different
types cannot overlap:

  * `([<x+y>+3]-1)` makes sense because each set of brackets contains or is contained by another set.
  * `([<x+y>+3)-1]` makes no sense because the parentheses and the square brackets overlap.

Given a string expression that can contain four types of brackets: `() <> []
{}`, create a function that returns `True` if the bracket logic is valid and
`False` if it is not.

### Examples

    bracket_logic("[<>()]") ➞ True
    
    bracket_logic("[<(>)]") ➞ False
    
    bracket_logic("[(a*b+<7-c>+9]") ➞ False
    # Opening parenthesis has no mate.
    
    bracket_logic("[{(h*i+3)-12]/4*x+2}") ➞ False
    # Square and curly brackets overlap.
    
    bracket_logic("[ab(c/d<e-f+(7*6)>)+2]") ➞ True

### Notes

Any characters other than the brackets can be ignored.

"""

def bracket_logic(xp):
  open_brackets = ["[","{","(","<"]
  closed_brackets = ["]","}",")",">"]
  status_brackets = []
  for i in range(0,len(xp)):
    if xp[i] in open_brackets:
      status_brackets.append(xp[i])
    elif xp[i] in closed_brackets:
      if len(status_brackets) == 0:
        return False
      elif open_brackets.index(status_brackets[-1]) == closed_brackets.index(xp[i]):
        status_brackets.pop(-1)
      else:
        return False
  return bool(len(status_brackets) == 0)

