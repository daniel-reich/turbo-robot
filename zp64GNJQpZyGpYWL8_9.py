"""


 **Nesting level** , in this challenge, refers to the depth of parentheses
around an integer. For example, in the string `"(5((10)8))"`, 5 has a nesting
level of 1 because it has one set of parentheses around it, 10 has a nesting
level of 3 because it has 3 sets of parentheses around it, and 8 has a nesting
level of 2.

We can score this string by multiplying each number times its nesting level
and then summing the results:

    "(5((10)8))" ➞ 5*1 + 10*3 + 8*2 ➞ 51

Create a function that takes a string as its argument and returns its score.

### Examples

    score_it("()") ➞ 0
    
    score_it("4(123)") ➞ 123
    # 4*0 + 123*1 = 123
    
    score_it("((((1)2)3)4)") ➞ 20
    # 1*4 + 2*3 + 3*2 + 4*1 = 20
    
    score_it("(6)8((34(7)))") ➞ 95
    # 6*1 + 8*0 + 34*2 + 7*3 = 95

### Notes

  * The nesting for all test cases is balanced and logically consistent (there are no missing or extra parentheses).
  * Test cases contain only positive integers.

"""

import re
def score_it(s):
  lst = re.findall('\d+|\(+|\)+', s)
  res = 0
  d = 0
  for i in lst:
    if i.isdigit():
      res += int(i)*d
    elif '(' in i:
      d += len(i)
    elif ')' in i:
      d -= len(i)
  return res

