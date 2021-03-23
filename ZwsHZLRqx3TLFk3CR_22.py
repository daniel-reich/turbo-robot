"""


Create a function that takes a list of factorial expressions and returns the
sum.

### Examples

    eval_factorial(["2!", "3!"]) ➞ 8
    
    eval_factorial(["5!", "4!", "2!"]) ➞ 146
    
    eval_factorial(["0!", "1!"]) ➞ 2

### Notes

0! and 1! both equal 1.

"""

def eval_factorial(li1):
     li2=  [i.replace('!','') for i in li1 ]
     newlist=[]
     for j in li2:
         if int(j)>1:
          for i in range(1,int(j)):
             j= int(j)*i
          newlist.append(j)
​
         else:
             newlist.append(1)
​
​
     return(sum(newlist))

