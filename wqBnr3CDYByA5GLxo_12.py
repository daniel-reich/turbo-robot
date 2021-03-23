"""


Write a function that takes in a string and returns all possible combinations.
Return the final result in **alphabetical order**.

### Examples

    unravel("a[b|c]") ➞ ["ab", "ac"]
    
    unravel("a[b|c]de[f|g]") ➞ ["abdef", "acdef", "abdeg", "acdeg"]
    
    unravel("a[b]c[d]") ➞ ["abcd"]
    
    unravel("a[b|c|d|e]f") ➞ ["abf", "acf", "adf", "aef"]
    
    unravel("apple [pear|grape]") ➞ ["apple grape", "apple pear"]

### Notes

Think of each element in every block (e.g. `[a|b|c]`) as a **fork in the
road**.

"""

import re
​
def unravel(txt):
  output = [""]
  while True:
    res = re.split("(\[[^\]]+\])", txt, 1)
    output = [pos + res[0] for pos in output]
    if len(res) == 1:
      break
    choices = re.split("\|", res[1][1:-1])
    output = [pos + choice for pos in output for choice in choices]
    txt = res[2]
  output.sort()
  return output

