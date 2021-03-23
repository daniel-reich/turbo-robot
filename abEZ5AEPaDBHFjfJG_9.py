"""


Create a function that takes a string and returns `True` or `False` depending
on whether or not the given formula is correct.

### Examples

    formula("6 * 4 = 24") ➞ True
    
    formula("18 / 17 = 2") ➞ False
    
    formula("") ➞ None

### Notes

  * You have to figure out what `a` is.
  * Ignore the spaces.
  * If the input is an empty string `""`, return `None`.
  * You do not need to dynamically find the value of `a` (it's a constant and the same accross all tests).

"""

import re
def eval_expr(string):
    regex_map = [(r'^\s*(([0-9]*[.])?[0-9]+)\s*$', lambda x: x.group(1)),
             (r'\([^()]+\)', lambda x: eval_expr(x.group(0)[1:-1])),
             (r'(.+)\+(.+)', lambda x: str(float(eval_expr(x.group(1))) +float(eval_expr(x.group(2))))),
             (r'(.+)\-(.+)', lambda x: str(float(eval_expr(x.group(1))) -float(eval_expr(x.group(2))))),
             (r'(.+)\*(.+)', lambda x: str(float(eval_expr(x.group(1))) *float(eval_expr(x.group(2))))),
             (r'(.+)\/(.+)', lambda x: str(float(eval_expr(x.group(1))) /float(eval_expr(x.group(2)))))]
    for op, fun in regex_map:
        string = re.sub(op, fun, string)
    return string
    
def formula(txt):
    if txt:
        chunks = [eval_expr(chunk) for chunk in txt.replace('a','4').split('=')]
        return all(float(num1)==float(num2) for num1,num2 in zip(chunks, chunks[1:]))

