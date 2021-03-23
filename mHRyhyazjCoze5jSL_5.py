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
  lista=[]
  for char in txt:
    if char==c1:
      lista.append(c2)
    elif char==c2:
      lista.append(c1)
    else:
      lista.append(char)
  return "".join(lista)

