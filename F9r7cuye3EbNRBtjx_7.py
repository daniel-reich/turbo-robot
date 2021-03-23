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

def string_builder(s):
  q, num_q = [''], []
  for i,c in enumerate(s):
    if c.isdigit():
      if s[i-1].isdigit():
        num_q[-1] += c
      else:
        num_q.append(c)
    elif c == '[':
      q.append('')
    elif c == ']':
      x = q.pop()
      q[-1] += x*int(num_q.pop())
    else:
      q[-1] += c
  return q[-1]

