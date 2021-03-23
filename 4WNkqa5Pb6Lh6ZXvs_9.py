"""


You will be given a polynomial expression in string form. The expression will
contain any of the following operations, written using standard mathematical
notation for a single variable, "x", as illustrated in the examples below:

  * addition: x + 1
  * subtraction: x – 2
  * multiplication: 3x
  * division: x / 4
  * exponentation: x^5
  * brackets: x(x + 1)

Your task is to write a function that can evaluate such a polynomial for a
given value of x. You will receive two arguments: the polynomial string and
the input number.

If the mathematical expression contains an error, you should return
`"invalid"`.

### Examples

    evaluate_polynomial("x+1", 5) ➞ 6
    
    evaluate_polynomial("5x^2", 3) ➞ 45
    
    evaluate_polynomial("(x(x+1))/2", 4) ➞ 10
    
    evaluate_polynomial("4(x + 3))/2", 5) ➞ "invalid"
    # Invalid because parentheses not balanced.

### Notes

The string will not contain spaces.

"""

import re
​
def format_mul(s):
    if s[-1]=='x' and s[-2].isdigit():
        return s[:-1]+'*'+'x'
    elif (s[-2]=='x' or s[-2]==')' or s[-2].isdigit())and s[-1]=='(':
        return s[:-1]+'*'+s[-1]
    else:
        return s
​
def format_text(text, n):
    text = re.sub(r'([\d.]+x)', lambda x: format_mul(x.group()),text)
    text = re.sub(r'[x\)\d]+\(', lambda x: format_mul(x.group()),text)
    text = re.sub(r'\^', "**",text)
    text = re.sub(r'x', str(n),text)
    
    return text
​
def evaluate_polynomial(text, n):
    length = len(text)
    if length == 0:
        return "invalid"
    
    count = 0
    valid_set = {'(',')','*','^','+','-','/','x'}
    for i in range(length):
        if (not text[i].isdigit()) and text[i] not in valid_set:
            return "invalid"
        if (i+1) <= (length-1):
            if text[i] == '/' and text[i+1] == '/':
                return "invalid"
    
    for i in range(length):
        if text[i] == '(':
            count += 1
        elif text[i] == ')':
            count = count -1
        if count < 0:
            return "invalid"
    if count != 0:
        return "invalid"
    
    text = format_text(text,n)
    #print(text)
​
    return eval(text)

