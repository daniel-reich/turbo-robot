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
  def good_or_perfect(l):
    if l%2 == 0:
      return 'good cut'
    else:
      return 'perfect cut'
  
  class Diamond:
​
    def __init__(self, carat):
      self.c = carat
      self.cut = good_or_perfect(carat)
​
      if self.cut == 'good cut':
        self.rnum = carat - 1
        self.cnum = carat
      else:
        self.rnum = carat
        self.cnum = carat
​
      self.cols = []
​
      def make_half(rowlen, collen):
        half = int(rowlen/2) + 1
        rows = []
        index = 0
        for n in range(half):
          row = []
          first = False
          for num in range(collen):
            if first == False:
              if num == index:
                row.append(1)
                index += 1
                first = True
              else:
                row.append(0)
            else:
              if num == collen - index:
                row.append(1)
              else:
                row.append(0)
          rows.append(row)
        
        return rows
      
      half_rows = make_half(self.rnum, self.cnum)
​
      self.rows = list(reversed(half_rows[1:])) + half_rows
      
      for n in range(self.cnum):
        col = []
        for row in self.rows:
          col.append(row[n])
        self.cols.append(col)
​
  d = Diamond(carat)
​
  return [d.rows, d.cut]

