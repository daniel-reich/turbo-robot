"""


You are a skilled diamondsmith whose business is getting better by the day.
Eventually, you decided that you needed to scale to keep up with demand.

  * Build a diamond-cutting machine (i.e. write a function that takes in a positive integer representing the raw stone's carat).
  * The output would be the finished diamond and tag indicating its quality, arranged in a list of two elements.
  * The first element would be a list of lists representing the diamond.
  * The second element would be a string indicating "perfect cut" if all the diamond's edges are pointy or "good cut" otherwise.

### Examples

    diamond(3) ➞ [
      [[0, 1, 0],
      [1, 0, 1],
      [0, 1, 0]],
      "perfect cut"
    ]
    
    # Perfect edge.
    diamond(4) ➞ [
      [[0, 1, 1, 0],
      [1, 0, 0, 1],
      [0, 1, 1, 0]],
      "good cut"
    ]
    
    # First and last rows had blunt edges with two 1s each.
    diamond(11) ➞ [
      [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]],
      "perfect cut"
    ]

### Notes

  * Cut is more important than carat in the diamondsmith's world. Hence, to reduce the number of blunt edges, the machine would reduce the size of the diamond.
  * In the second example of a 4-carat raw stone, the machine produces a finished diamond of only 3 rows so that there would only be 2 blunt edges, instead of 4.
  * In the first and third examples, the machine was able to produce diamonds of n-rows from n-carat stones.

"""

def diamond(carat):
  width = carat // 2 + carat % 2
  diamond = [[0 for i in range(width)] for i in range(width)]
  for i in range(width):
    diamond[i][i] = 1
  if carat%2 == 0:
    diamond = [row[::-1] + row for row in diamond]
  else:
    diamond = [row[:0:-1] + row for row in diamond]
  diamond += [diamond[i] for i in range(width-2, -1, -1)]
  return [diamond, 'perfect cut' if carat % 2 else 'good cut']

