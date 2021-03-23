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
    if(txt==""):
        return []
    ic=0
    dis=0
    n=0
    lst1=[]
    lst2=[]
    for i in range(0,len(txt)):
        if(ic!=0 and dis!=0 and ic==dis):
            lst1.append(i)
            ic=0
            dis=0
        if(txt[i]=='('):
            ic+=1
        if(txt[i]==')'):
            dis+=1
    if(lst1==[]):
        lst1.append(txt)
        return lst1
    else:
​
​
        for i in range(0,len(lst1)):
            temp=""
            for k in range(n,lst1[i]):
                temp+=txt[k]
                n+=1
            lst2.append(temp)
        temp2=""
        for i in range(lst1[len(lst1)-1],len(txt)):
            temp2+=txt[i]
        lst2.append(temp2)
​
        return lst2

