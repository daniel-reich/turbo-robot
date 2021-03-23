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
def string_builder(s):
    while ']' in s:
        pat = r'(\d+)\[(\w+)\]'
        s = re.sub(pat,lambda x: int(x.group(1)) * x.group(2),s)
    return s

