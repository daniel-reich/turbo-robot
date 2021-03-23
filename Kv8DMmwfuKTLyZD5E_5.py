"""


Create a function which creates a square dartboard of side length `n`. The
value of a number should increase, the closer it is to the centre of the
board.

### Examples

    make_dartboard(3) ➞ [
      111,
      121,
      111
    ]
    
    make_dartboard(8) ➞ [
      11111111,
      12222221,
      12333321,
      12344321,
      12344321,
      12333321,
      12222221,
      11111111
    ]
    
    make_dartboard(5) ➞ [
      11111,
      12221,
      12321,
      12221,
      11111
    ]

### Notes

If the size given is an even number, the centre should be made up of the 4
highest values.

"""

def make_dartboard(n):
    k=0
    g=sorted([a for a in range (4*(1+(n%2==1)),n*4,8)],reverse=True)
    g.append(1)
    m = ['0' * n for i in range(n)]
    x0, y0 = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += x0[i % 4]
            y += y0[i % 4]
            m[x]=m[x][:y]+str(c)+m[x][y+1:]
            k+=1
            if k==g[c-1]:
                k=0
                c+=1 
    return [int(i) for i in m]

