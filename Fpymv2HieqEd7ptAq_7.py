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
    new_element = ''
    new_list = []
    for elem in txt:
        new_element += elem
        if elem == '(':
            count += 1
        if elem == ')':
            count -= 1
        if count == 0:
            new_list.append(new_element)
            new_element = ''
    return new_list

