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
    #brainstorm#
    expecting = [] #latest (-1) is the one that the parser is expecting to be correct
    pOpening = '(<[{'
    pClosing = ')>]}'
    pExchange = {'(':')', '<':'>','[':']','{':'}'}
    print(xp)
    for _ in xp:
        print(expecting)
        if _ in pOpening:
            expecting.append(_)
        if _ in pClosing:
            if len(expecting) > 0:
                if pExchange[expecting[-1]] == _:
                    expecting.pop()
                else:
                    return False
            else:
                return False
    if len(expecting) > 0:
        return False 
    return True

