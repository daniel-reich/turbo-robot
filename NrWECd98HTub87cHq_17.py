"""


Create a function that returns the area of the overlap between two rectangles.
The function will receive two rectangles, each with the coordinates of the
lower left corner followed by the width and the height `rect = [x, y, width,
height]`.

### Examples

    overlapping_rectangles([ 2, 1, 3, 4 ], [ 3, 2, 2, 5 ]) ➞ 6
    
    overlapping_rectangles([ 2, -9, 11, 5 ], [ 5, -11, 2, 9 ]) ➞ 10
    
    overlapping_rectangles([ -8, -7, 4, 7 ],  [-5, -9, 4, 7 ]) ➞ 5

![Example 1](https://edabit-challenges.s3.amazonaws.com/ex1.png)

![Example 2](https://edabit-challenges.s3.amazonaws.com/ex2.png)

![Example 3](https://edabit-challenges.s3.amazonaws.com/ex3.png)

### Notes

  * Coordinates can be positive or negative integers.
  * Not all examples have overlaps.

"""

def overlapping_rectangles(rect1, rect2):
    x,y=0,0
    if rect1[0]<rect2[0]:L,R=rect1,rect2   
    else:R,L=rect1,rect2 
    if L[0]+L[2]>=R[0]:x=min(L[0]+L[2],R[0]+R[2])-max(L[0],R[0])
    if L[1]<=R[1] and L[1]+L[3]>R[1] or L[1]>=R[1] and R[1]+R[3]>L[1]:
        y=min(R[1]+R[3],L[1]+L[3])-max(L[1],R[1])
    return x*y

