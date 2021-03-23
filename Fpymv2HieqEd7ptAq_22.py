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
    count = 0
    new = []
    temp = ""
    for c in txt:
        if c == "(":
            count += 1
            temp += "("
        else:
            if count == 1:
                temp += ")"
                new.append(temp)
                temp = ""
                count = 0
            else:
                temp += ")"
                count -= 1
    return new

