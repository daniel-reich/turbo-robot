"""


Write a function to replace all instances of character `c1` with character
`c2` and vice versa.

### Examples

    double_swap("aabbccc", "a", "b") ➞ "bbaaccc"
    
    double_swap("random w#rds writt&n h&r&", "#", "&")
    ➞ "random w&rds writt#n h#r#"
    
    double_swap("128 895 556 788 999", "8", "9")
    ➞ "129 985 556 799 888"

### Notes

Both characters will show up at least once in the string.

"""

def double_swap(txt, c1, c2):
  output = ""
  for char in txt:
    if char not in [c1, c2]:
      output += char
    else:
      if char == c1:
        output += c2
      else:
        output += c1
  return output

