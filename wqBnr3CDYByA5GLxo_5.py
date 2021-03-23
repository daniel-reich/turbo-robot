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

def unravel(txt):
  unravelled = []
  remaining = [(txt, '')]
  while len(remaining) != 0:
    nextrem = remaining.pop(0)
    start = nextrem[0].find('[')
    if start != -1:
      close = nextrem[0].find(']')
      options = nextrem[0][start+1:close].split('|')
      for o in options:
        remaining.append((nextrem[0][close+1:], \
                          nextrem[1]+nextrem[0][:start]+o))
    else:
        unravelled.append(nextrem[1]+nextrem[0])
  return sorted(unravelled)

