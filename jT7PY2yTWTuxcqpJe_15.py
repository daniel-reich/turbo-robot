"""


Given a matrix of m * n elements (m rows, n columns), return all elements of
the matrix in spiral order.

### Examples

    spiral_order([
      [ 1, 2, 3 ],
      [ 4, 5, 6 ],
      [ 7, 8, 9 ]
    ]) ➞ [1, 2, 3, 6, 9, 8, 7, 4, 5]
    
    spiral_order([
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]) ➞ [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

### Notes

NA

"""

def spiral_order(m):
    s = []
​
    def empty(m):
        try:
            x = m [0]
            return False
        except:
            return True
        
    while not empty(m):
        for x in range(len(m [0])):
            s.append(m [0][x])
        m.pop(0)
        if not empty(m):
            for x in range(len(m)):
                s.append(m [x][len(m [x])-1])
                m [x].pop(len(m [x])-1)
​
            if not empty(m):
​
                for x in reversed(range(len(m [len(m)-1]))):
                    s.append(m [len(m)-1][x])
                m.pop(len(m)-1)
​
                if not empty(m):
​
                    for x in reversed(range(len(m))):
                        s.append(m [x][0])
                        m [x].pop(0)
​
    return s

