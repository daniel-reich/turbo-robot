"""


Consider a right triangle. Its area and hypotenuse are known.

Create a function that returns the two missing sides. The first input is the
area and the second input is the hypotenuse. Return your answer as a list (the
shorter side first). If there is no such right triangle, return `"Does not
exist"`.

### Examples

    f(3, 6) ➞ [1.015, 5.914]
    
    f(30, 12) ➞ [5.675, 10.574]
    
    f(30, 10) ➞ "Does not exist"

### Notes

Round your answer to three decimal places.

"""

def f(a, h):
    y=0
    while y**4-y*y*h*h+4*a*a>0 and y<h:
        y+=1/100     
    while y**4-y*y*h*h+4*a*a<0 and y<h:
        y-=1/100000
    if y<=0 or y>=h: return "Does not exist"
    x=2*a/y
    return sorted([round(x,3),round(y,3)])

