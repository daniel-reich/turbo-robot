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
  single, multiple, opened, closed = [], [], 0, 0
  for i in txt:
    if i == "(":
      opened += 1
      single.append(i)
    else:
      closed += 1
      single.append(i)
    if opened == closed:
      opened, closed = 0, 0
      cluster = "".join(single)
      multiple.append(cluster)
      single.clear()
​
  return(multiple)

