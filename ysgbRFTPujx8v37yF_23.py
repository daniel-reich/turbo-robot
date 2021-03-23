"""


Imagine this triangle:

        1
       2 3
      4 5 6
     7 8 9 10
    ...

Create a function that takes a number `n` and returns the sum of all numbers
in **nth row**.

### Examples

    row_sum(1) ➞ 1
    
    row_sum(2) ➞ 5
    
    row_sum(4) ➞ 34

### Notes

1 <= N <= 1000

"""

def row_sum(n):
    # 1, 2, 3, 4, 5, 6
    # 1, 3, 6, 10,15,21
    up = 2;
    C = 1;
    stop = 0;
    for i in range(1,n):
        if i == n-1:
            stop = C
        C += up;
        up+=1
​
    W = (C * (C + 1))/2
    return W - ((stop * (stop + 1))/2)

