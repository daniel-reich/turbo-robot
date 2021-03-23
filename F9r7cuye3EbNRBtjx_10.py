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
​
def string_builder(s):
    pattern = "([1-9][0-9]*)\[(\w*)\]"
    substitute = lambda m: m.group(2)*(int(m.group(1)))
    result = s
    while True:
        new_result = re.sub(pattern, substitute, result)
        if new_result == result:
            break
        else:
            result = new_result
    return(result)

