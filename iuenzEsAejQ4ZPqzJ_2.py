"""


This is a **reverse coding challenge**. Normally you're given explicit
directions with how to create a function. Here, you must generate your own
function to satisfy the relationship between the inputs and outputs.

Your task is to create a function that, when fed the inputs below, produce the
sample outputs shown.

### Examples

    3 ➞ 21
    
    9 ➞ 2221
    
    17 ➞ 22221
    
    24 ➞ 22228

### Notes

If you get stuck, check the **Comments** for help.

"""

def mystery_func(num):
  l=[]
  for i in range(1,num):
    if(pow(2,i)<=num):
      l.append(i)
  m=max(l)
  r=num-pow(2,m)
  a='2'*m+str(r)
  return int(a)

