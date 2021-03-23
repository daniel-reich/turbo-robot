"""


Create a function that takes a mathematical expression in **prefix notation**
as a string and evaluates the expression.

### Examples

    prefix("+ 5 4") ➞  9
    
    prefix("* 12 2") ➞  24
    
    prefix("+ -10 10") ➞  0

### Notes

  * The mathematical expression is valid.
  * Check the **Resources**.
  * Use `//` for division.

"""

def prefix(exp):
 items = exp.replace('/','//').split(' ')
 i = len(items)-1
 while i>=0:
  if items[i] in '*+-//':
   items[i:i+3] = [str(eval("({}){}({})".format(items[i+1],items[i],items[i+2])))]
  i-=1
 return int(items[0])
is_exact = lambda n, k=1, i=1: is_exact(n, k*i, i+1) \
 if k < n else ([n, i-1] if k == n else 'Not exact!')

