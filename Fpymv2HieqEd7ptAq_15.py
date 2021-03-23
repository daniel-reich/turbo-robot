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
  a = 0
  b = 0
  c = 0
  lst = []
  for i in txt:
    if i=='(' : a+=1
    elif i==')' : b+=1
    if a==b :
      lst.append(txt[c:c+a+b])
      c+=a +b 
      a = 0
      b = 0
  return lst

