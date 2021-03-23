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
  if len(s)==0: return ''
  if s[0]>'9': return s[0]+string_builder(s[1:])
  tmp= s.find(']')
  while s[:tmp].count('[') > s[:tmp+1].count(']'):
    tmp=s.find(']',tmp+1)
  
  st=1
  if s[1]<='9': st=2
  return string_builder(s[st+1:(tmp)]*int(s[0:st])) + string_builder(s[tmp+1:])

