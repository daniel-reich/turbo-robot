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
  valid = True;
  scope = []
  obrackets = list("(<[{")
  cbrackets = list(")>]}")
  # () <> [] {}
  for i in xp:
    if (i in obrackets):
      scope.append(i)
    elif (i in cbrackets):
      if (not chr(ord(i)-[2, 1][i == ")"]) == scope[-1]):
        print(chr(ord(i)-[2, 1][i == ")"]))
        valid = False;
        break;
      else:
        del scope[-1]
  if (len(scope)):
    valid = False;
  return valid

