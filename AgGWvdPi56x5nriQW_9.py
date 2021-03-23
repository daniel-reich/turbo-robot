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

def longest_slide(s):
    for i in range(1, len(s)):
        l = []
        for ii in range(len(s[i])):
            if ii == 0:
                l.append(s[i-1][0] + s[i][ii])
            elif ii == len(s[i]) - 1:
                l.append(s[i-1][-1] + s[i][ii])
            else:
                l.append(max(s[i-1][ii-1:ii+1]) + s[i][ii])
        s[i] = l
    return max(s[-1])

