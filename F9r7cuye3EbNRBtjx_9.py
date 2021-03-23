"""


The function is given a string with some square brackets in it. You need to
build the outcome string using the rule: `k[substring]` is replaced by the
`substring` inside the square brackets being repeated exactly `k` times.

### Examples

    string_builder("3[a]2[bc]") ➞ "aaabcbc"
    
    string_builder("3[a2[c]]") ➞ "accaccacc"
    
    string_builder("2[abc]3[cd]ef") ➞ "abcabccdcdcdef"

### Notes

`k` is a positive integer.

"""

import re
expr = re.compile(r'(\d+)\[([^\[\]]+)\]')
​
def string_builder(s):
  while True:
    m = expr.search(s)
    if not m:
      break
    count, substring = int(m.group(1)), m.group(2)
    s = s[:m.start()] +  substring * count + s[m.end():]
  return s

