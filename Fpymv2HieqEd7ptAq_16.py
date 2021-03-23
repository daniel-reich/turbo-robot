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
    balance = 0
    split_parentheses, curr = [], []
    opening, closing, balanced = "(", ")", 0
    for parenthesis in txt:
        curr.append(parenthesis)
        if parenthesis == opening:
            balance += 1
        else:
            balance -= 1
        if balance == balanced:
            split_parentheses.append("".join(curr))
            curr = []
    return split_parentheses

