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
    if n == 0:
        return []
    result = ["1"] * n
    if n % 2 == 0:
        result[0] = int("1" * n)
        for i in range(1, n // 2):
            result[i] = result[i - 1] + int("1" * (n - 2 * i) + "0" * i)
        for i in range(n // 2, n):
            result[i] = result[n - 1 - i]
    elif n % 2 != 0:
        result[0] = int("1" * n)
        for i in range(1, n // 2 + 1):
            result[i] = result[i - 1] + int("1" * (n - 2 * i) + "0" * i)
        for i in range(n // 2 + 1, n):
            result[i] = result[n - 1 - i]
    return result

