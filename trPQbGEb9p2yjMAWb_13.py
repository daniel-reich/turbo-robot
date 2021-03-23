"""


In this challenge, you have to verify that every, or some, of the given
variables, pass a given test condition. There are seven parameters:

  * `test`: A string being the condition to verify.
  * `val`: A string with two possible values:
    * `everybody` if **every** variable has to pass the test;
    * `somebody` if **at least one** of the variables has to pass the test.
  * `a`, `b`, `c`, `d`, `e`: The variables being integers or booleans.

Create a function that returns `True` or `False`, depending on the result of
the test applied to the variables.

### Examples

    every_some(">= 1", "everybody", 1, 1, -1, 1, 1) ➞ False
    # Is every variable >= 1?
    
    every_some(">= 1", "somebody", -1, -1, -1, -1, 1) ➞ True
    # Is some variable >= 1?
    
    every_some("< 4 / 2", "everybody", 1, 2, 1, 0, -10) ➞ False
    # Is every variable < 2?

### Notes

N/A

"""

def every_some(expr, option, *args) -> bool:
    L = [str(i) + ' ' + expr for i in args]
    if option == "everybody":
        return all(eval(i) for i in L)
    else:
        return any(eval(i) for i in L)

