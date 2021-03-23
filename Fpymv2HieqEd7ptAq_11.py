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
  result = []
  open_count = 0
  closed_count = 0
  
  subset = ""
  
  for char in txt:
    if char == "(":
      subset += "("
      open_count += 1
    if char == ")":
      subset += ")"
      closed_count += 1
      if closed_count == open_count:
        result.append(subset)
        subset = ""
  
  return result

