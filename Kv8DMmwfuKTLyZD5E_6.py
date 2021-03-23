"""


Create a function which creates a square dartboard of side length `n`. The
value of a number should increase, the closer it is to the centre of the
board.

### Examples

    make_dartboard(3) ➞ [
      111,
      121,
      111
    ]
    
    make_dartboard(8) ➞ [
      11111111,
      12222221,
      12333321,
      12344321,
      12344321,
      12333321,
      12222221,
      11111111
    ]
    
    make_dartboard(5) ➞ [
      11111,
      12221,
      12321,
      12221,
      11111
    ]

### Notes

If the size given is an even number, the centre should be made up of the 4
highest values.

"""

import math
def dartboard(i,n):
    for i in range(1,n+1):
        row='{:0^{}}'.format('1'*i,n)
    return row       
def make_dartboard(n):
    x,y,b=[],[],''
    m=math.ceil(n/2)
    for i in range(1,m+1):
        x.append(dartboard(i,n))
    y.append(x[0])
    x=x[0::]
    i=0
    while len(x)>len(y):
        a=y[i]
        i+=1
        e=a[i:-i]
        c=a[:i]
        for j in e:
            j=int(j)+1
            b+=str(j)
        z=c[::-1]   
        d=str(c)+b+str(z) 
        y.append(d)
        b=''
    if n%2==0:    
        p=y
    else:
        p=y[0:-1]
    return [int(i)for i in(y+p[::-1])]

