"""


The goal of this challenge is to return Pascal's triangle up to number 29.
Pascal's triangle is the sum of the two upper corners.

       1 1
      1 2 1
     1 3 3 1
    
    # There will always be the 1 in the first
    # place and the row in the second.

![Pascal's Triangle](https://edabit-
challenges.s3.amazonaws.com/PascalTriangleAnimated2.gif)

Create a function that returns a row from Pascal's triangle. To find the row
and column you can use `n!/(k!*(n-k)!)` where `n` is the row down and `k` is
the column.

### Examples

    pascals_triangle(1) ➞ "1 1"
    
    pascals_triangle(4) ➞ "1 4 6 4 1"
    
    pascals_triangle(6) ➞ "1 6 15 20 15 6 1"
    
    pascals_triangle(8) ➞ "1 8 28 56 70 56 28 8 1"

### Notes

N/A

"""

def pascals_triangle(row):
  if (row ==1):
    return "1 1"
  else:
    list2 = "1"
    for k in range (1,row):
      elem = fact(row)/(fact(k)*fact(row-k))
      list2 +=" " + str(int(elem))
      list3  = list2 + " 1"
    return(list3)
        
def fact (a):
    if ( a == 1 or a == 0):
        return 1
    else:
        temp = 0
        res = 1
        while ( a !=1):
            temp = a
            res *= temp * ( temp-1)
            if ( a-2 == 0):
                break
            else:
                a -=2
    return(res)

