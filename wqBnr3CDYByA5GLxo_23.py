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
import itertools
​
def generate(x):
  if len(x) >= 1 and x[0] == '[':
    elms = x[1:-1].split('|')
    for e in elms:
      yield e
  else:
    yield x
​
def unravel(txt):
  chunks = re.split(r'(\[.*?\])', txt)
​
  gens = []
  for c in chunks:
    gens.append([e for e in generate(c)])
​
  results = []
  for t in itertools.product(*gens):
    results.append(''.join(t))
​
  return sorted(results)

