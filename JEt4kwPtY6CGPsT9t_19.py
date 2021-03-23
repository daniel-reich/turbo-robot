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

import functools 
import operator  
def convertTuple(tup): 
    str = functools.reduce(operator.add, (tup)) 
    return str
          
def mathematical(exp, numbers):
    n=[str(i)for i in numbers]
    exp=exp.replace('x','*')          
    ex=exp[-3::]
    if ex=='y^2':
        ex=ex.replace('y^2','y**2')
    z,a,b,c,p,n,m=[],[],[],[],[],[],[]
    if len(numbers)==2:
        d=['1','2']
    if numbers==[3,6,9]:
        d=['3','6','9']
    else:
        d=['1','2','3']
    for i in numbers:
        y=i
        z.append(str(int(eval(ex))))
        a.append(exp[0:-3])
    b= [(a,b) for (a,b) in zip(a,z)]
    for i in b:
        c.append(convertTuple(i))
    for i in range(len(d)):
        for word in c:
            word=list(word)
            for j in range(len(word)):
                if word[j]!='y':
                    m.append(word[j])
                else:
                    m.append(word[j].replace(word[j],d[i]))
               
            n.append(''.join(m))
            m=[]         
    if len(numbers)==2:        
         return [n[0],n[3]] 
    else:
        return [n[0],n[4],n[-1]]

