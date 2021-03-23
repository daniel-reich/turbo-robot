"""


You are counting points for a basketball game, given the amount of 3-pointers
scored and 2-pointers scored, find the final points for the team and return
that value ([2 -pointers scored, 3-pointers scored]).

### Examples

    points(1, 1) ➞ 5
    
    points(7, 5) ➞ 29
    
    points(38, 8) ➞ 100

### Notes

N/A

"""

points = lambda a,b:a*2 + (b*3)

