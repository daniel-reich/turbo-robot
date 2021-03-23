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
    i = n % 2
    d = n // 2 + 1
    res = [str(d)] if i else []
    while True:
        i += 2
        d -= 1
        if i > n: return list(map(int, res))
        sd = str(d)
        res = [sd*i] + [sd + row + sd for row in res] + [sd*i]

