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
  
  temp,res="",[]
  counter,i=0,0
  while i<len(txt):
    temp+=txt[i]
    if txt[i]=="(":
      counter+=1
    elif txt[i]==")":
      counter-=1
    
    if counter==0:
      res.append(temp)
      temp=""
    i+=1
  return res

