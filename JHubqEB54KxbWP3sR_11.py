"""


Given the formula for a straight line `y = ax + b` and the x, y coordinates of
a point, find the distance between that point and the line. Round the result
to two decimal points.

### Examples

    dist("y=(-3/4)x-5/4", 5, 2) ➞ 5.6
    
    dist("y=(5+1/3)x-2.3", 1, 4) ➞ 0.18
    
    dist("y=2.2x-(3+1/5)", 3, -2) ➞ 2.23

### Notes

Check the **Resources**.

"""

def dist(line, x, y):
    record=0
    record2=0
    m=''
    b=''
    for character in line:
        if record==1:
            m+=character
        if character=='=':
            record=1
        if character=='x':
            record=0
            m=m.replace('x','')
    m2=eval(m)
    for character in line:
        if record2==1:
            b+=character
        if character=='x':
            record2=1
    b2=eval(b)
    perpm=-1/m2
    perpb=y-perpm*x
    intx=(perpb-b2)/(m2-perpm)
    inty=(m2*intx+b2)
    return round((((x-intx)**2+(y-inty)**2)**.5)*100)/100

