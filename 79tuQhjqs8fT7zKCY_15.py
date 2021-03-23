"""


Postfix notation is a mathematical notation in which operators follow their
operands. In other words, `pfexp1 pfexp2 op`, where `pfexp1` and `pfexp2` are
both postfix expressions.

Some examples:

  * `2 2 +` is the postfix notation of the expression `2 + 2`.
  * `2 3 * 1 - 5 /` is the postfix notation of the expression `((2 * 3) - 1) / 5`.

Here you have to compute the result from a postfix expression.

### Examples

    postfix("2 2 +") ➞ 4
    # 2 + 2 = 4
    
    postfix("2 3 * 1 - 5 /") ➞ 1
    # ((2 * 3) - 1) / 5 = (6 - 1) / 5 = 5 / 5 = 1

### Note

  * Operators and operands are separated by a space.
  * The operators `+, -, *, /` may be supported.
  * You can use Python list as a stack data structure to solve this problem.

"""

def postfix(expr):
  a,b,c,d,e,f=[],[],[],[],[],[]
  
  if len(expr)==1:
    return(int(expr))
  
  expr=expr.split()
  
  if len(expr)==3:
    return (calc(expr))
  
  if len(expr)==5:
    return(calc([str(calc(expr))]+expr[3:]))  
  
  if len(expr)==7:
   a=calc(expr)
   b=[str(a)]+expr[3:]
   c=calc(b)
   if b[2]=="+" or b[2]=="-" or b[2]=="*" or b[2]=="/":
    d=[str(c)]+b[3:]
    return(calc(d))
   else:
    d=b[:1]+[str(c)]+b[4:]
    return(calc(d))
  
  if len(expr)>8:
   a=calc(expr)
   b=[str(a)]+expr[3:]
   c=calc(b)
   d=[str(c)]+b[3:]
   e=calc(d)
   f=d[:1]+[str(e)]+d[4:]
   return(calc(f))
 
def calc(a):
  if a[2]=="+" or a[2]=="-" or a[2]=="*" or a[2]=="/":
   return int(eval(a[0]+a[2]+a[1]))
  else:
   return int(eval(a[1]+a[3]+a[2]))

