"""


Create a function that takes a mathematical expression as a string, list of
numbers on which the mathematical expression is to be calculated and return
the result as a list of string.

### Examples

    mathematical("f(y)=y+1",[1,2]) ➞ ["f(1)=2","f(2)=3"]
    
    mathematical("f(y)=y^2",[1,2,3]) ➞ ["f(1)=1","f(2)=4","f(3)=9"]
    
    mathematical("f(y)=yx3",[1,2,3]) ➞ ["f(1)=3","f(2)=6","f(3)=9"]

### Notes

  * List of numbers are positive integers.
  * In the algebraic expression x = `*`

"""

def mathematical (exp, numbers):
    
    results =[] 
    ext_lst = []
    
    if '+'in exp:
        for i in numbers: 
            results.append(i + int(exp[-1])) 
            
    elif '^' in exp:
        for i in numbers:
            results.append(i ** int(exp[-1])) 
            
    elif 'x' in exp:
        for i in numbers:
            results.append(i * int(exp[-1])) 
    elif '-' in exp:
        for i in numbers:
            results.append(i - int(exp[-1]))
    elif '/' in exp:
        for i in numbers:
            results.append(int(i / int(exp[-1])))
            
    for j in range(len(numbers)):
        ext_lst.append("f({})={}".format(numbers[j], results[j]))
    
    return ext_lst

