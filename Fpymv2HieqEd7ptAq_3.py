"""


Write a function that groups a string into **parentheses cluster**. Each
cluster should be **balanced**.

### Examples

    split("()()()") ➞ ["()", "()", "()"]
    
    split("((()))") ➞ ["((()))"]
    
    split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]
    
    split("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]

### Notes

  * All input strings will **only** contain parentheses.
  *  **Balanced** : Every opening parens `(` must exist with its matching closing parens `)` in the same cluster.

"""

def split(txt):
  marker = 0
  s = []
  clusters = []
  
  for c in txt:
    if c == '(':
      s.append(c)
    elif c == ')':
      s.pop()
    marker += 1
    #..... EZ CLAP
    if len(s) == 0:
      clusters.append(txt[0: marker])
      txt = txt[marker:]
      marker = 0
  
  return clusters

