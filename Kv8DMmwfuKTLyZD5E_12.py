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
    result = ["1"*n]
    if n%2 == 0:
        for i in range(2,int(n/2)+1):
            result.append(result[-1][:i-1]+str(i)*(n-(len(result[-1][:i-1])*2))+(result[-1][:i-1])[::-1])
        return [int(i) for i in result+result[::-1]]
    else:
        for i in range(2,n//2+2):
            result.append(result[-1][:i-1]+str(i)*(n-(len(result[-1][:i-1])*2))+(result[-1][:i-1])[::-1])
        return [int(i) for i in result+result[:-1][::-1]]

