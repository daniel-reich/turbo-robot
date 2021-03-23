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
    m = n // 2 + n % 2
    s = ["1" * m]
    for i in range(1, m):
        add = s[-1][: i] + (m - i) * str(i + 1)
        s.append(add)
    if n % 2 == 1:
        s = [i[:-1] + i[::-1] for i in s]
        s = s[:-1] + s[::-1]
    else: 
        s = [i + i[::-1] for i in s]
        s = s + s[::-1]
    return [int(i) for i in s]

