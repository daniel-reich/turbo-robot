"""


Create a function that takes a list of pyramid numbers and returns the maximum
sum of consecutive numbers from the top to the bottom of the pyramid.

                            /3/
                            \7\ 4 
                           2 \4\ 6 
                          8 5 \9\ 3
    
    # Longest slide down sum is 3 + 7 + 4 + 9 = 23

### Examples

    longest_slide([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) ➞ 23
    
    longest_slide([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) ➞ 20
    
    longest_slide([[2], [9, 4], [1, 8, 7], [6, 4, 7, 2]]) ➞ 26

### Notes

N/A

"""

def longest_slide(p):
    for r in range(1, len(p)):
        for c in range(r + 1):
            if c == 0:
                p[r][c] += p[r - 1][c]
            elif c == r:
                p[r][c] += p[r - 1][c - 1]
            else:
                p[r][c] += max(p[r - 1][c - 1], p[r - 1][c])
    return max(p[-1])

