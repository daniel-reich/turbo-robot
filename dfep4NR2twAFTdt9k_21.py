"""


Create a function that multiplies two matricies (n x n each).

### Examples

    matrix_mult([[4, 2],[3, 1]], [[5, 6], [3, 8]]) ➞ [[26, 40], [18, 26]]
    
    matrix_mult([[3, 6],[4, 5]], [[8, 1], [7, 2]]) ➞ [[66, 15], [67, 14]]
    
    matrix_mult([[7, 5],[2, 2]], [[6, 7], [3, 2]]) ➞ [[57, 59], [18, 18]]

### Notes

Limit yourself to 2 x 2 matricies.

"""

def matrix_mult(m1, m2):
​
    matrix = ['','']
    
    matrix[0] =[[m1[0][0],m2[0][0]],[m1[0][1],m2[1][0]],[m1[0][0],m2[0][1]],[m1[0][1],m2[1][1]]]
​
    matrix[1] = [[m1[1][0],m2[0][0]],[m1[1][1],m2[1][0]],[m1[1][0],m2[0][1]],[m1[1][1],m2[1][1]]]
​
    lis = []
​
    for i in matrix:
        l1 = i[0][0] * i[0][1]
        l2 = i[1][0] * i[1][1]
​
        l3 = i[2][0] * i[2][1]
        l4 = i[3][0] * i[3][1]
​
        ans1 = l1 + l2
        ans2 = l3 + l4
​
        lis.append([ans1,ans2])
    
    return lis

