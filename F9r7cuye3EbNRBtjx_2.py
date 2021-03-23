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

from re import sub
def string_builder(s):
  s = sub(r'(\d+)(\[)([^\[\]]+)(\])',lambda x: int(x.group(1)) * x.group(3),s)
  if '[' in s:
    return string_builder(s)
  return s

