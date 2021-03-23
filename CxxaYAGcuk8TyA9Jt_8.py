"""


Write a function that takes a string of source code and checks whether the
braces/parentheses are balanced. Every `(` or `{` must be closed by a `}` or
`)` in the opposite order. Return the index at which an imbalance occurs, or
`-1` if the string is balanced. If any `(` or `{` are never closed, return the
string's length.

### Examples

    check_balance("if (a(4) > 9) { foo(a(2)); }") ➞ -1
    # Returns -1 because it's balanced.
    
    check_balance("for (i=0;i<a(3};i++) { foo{); )") ➞ 14
    # Returns 14 because } is out of order.
    
    check_balance("if (x) {")  ➞ 8
    # Returns 8 because { is never closed.

### Notes

Think about how you can leverage [Stack Data
Structure](https://www.geeksforgeeks.org/stack-in-python/).

"""

def check_balance(expression):
    if expression == "":
        return -1
    cnt_left_brace = 0
    cnt_right_brace = 0
    cnt_left_par = 0
    cnt_right_par = 0
    for i in range(len(expression)):
        if expression[i] == "(":
            cnt_left_brace +=1
        elif expression[i] == ")":
             cnt_right_brace += 1
             if cnt_right_brace > cnt_left_brace:
                 return i
             index_left_brace = expression.rfind("(", 0, i)
             index_left_par = expression.rfind("{", index_left_brace, i)
             index_right_par = expression.rfind("}", index_left_brace, i)
             if index_left_par != -1 and   index_right_par == -1:
                 return i
        elif expression[i] == "{":
                cnt_left_par +=1
        elif expression[i] == "}":
                cnt_right_par +=1
                if cnt_right_par > cnt_left_par:
                   return i
                index_left_par = expression.rfind("{", 0, i)
                index_left_brace = expression.rfind("(", index_left_par, i)
                index_right_brace = expression.rfind(")", index_left_par, i)
                if index_left_brace != -1 and index_right_brace == -1:
                    return i
    if cnt_left_brace != cnt_right_brace or cnt_left_par != cnt_right_par:
        return len(expression)
    return -1

