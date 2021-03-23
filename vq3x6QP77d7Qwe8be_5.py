"""


Create a function that takes an array of numbers, and returns the size of the
biggest square patch of odd numbers. See examples for a clearer picture.

### Examples

    odd_square_patch([
      [1, 2, 4, 9],
      [4, 5, 5, 7],
      [3, 6, 1, 7]
    ]) ➞ 2
    
    # The 2x2 square at the lower right
    # ([5, 7] on the 2nd row, [1, 7] on the third).
    
    odd_square_patch([[1, 2, 4, 9]]) ➞ 1
    
    # An array with a single row can only have a square patch of
    # maximum size 1x1 containing a single odd element.
    
    odd_square_patch([[2, 4, 6]]) ➞ 0

### Notes

N/A

"""

def odd_square_patch(lst):
  def is_odd(n):
    return n%2==1
  
  class Array:
    class Space:
​
      def __init__(self, val, odd, r, c):
        self.v = val
        self.odd = odd
        self.r = r
        self.c = c
    class ROC:
​
      def __init__(self, roc):
        self.roc = roc
        
        rows = set()
        cols = set()
​
        for item in roc:
         # print(item)
          row = item.r
          col = item.c
​
          rows.add(row)
          cols.add(col)
        
        rows = list(rows)
        cols = list(cols)
​
        if len(rows) == 1:
          cols = sorted(cols)
          self.sorted = []
          for col in sorted(cols):
            for item in roc:
              if item.c == col:
                self.sorted.append(item)
        elif len(cols) == 1:
          rows = sorted(rows)
          self.sorted = []
          for row in rows:
            for item in roc:
              if item.r == row:
                self.sorted.append(item)
        else:
          self.sorted = rows, cols
​
    def __init__(self, arr):
      self.arr = arr
      a = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
      
      self.spaces = {}
​
      for n in range(len(arr)):
        row_l8r = a[n]
        row = arr[n]
        for c in range(len(row)):
          val = row[c]
          odd = is_odd(val)
          self.spaces['{}{}'.format(row_l8r,c)] = Array.Space(val, odd, row_l8r, c)
      
      self.rows = {}
      self.cols = {}
​
      for space in self.spaces.keys():
        row = space[0]
        col = space[1]
​
        if row not in self.rows.keys():
          self.rows[row] = [self.spaces[space]]
        else:
          self.rows[row].append(self.spaces[space])
        
        if col not in self.cols.keys():
          self.cols[col] = [self.spaces[space]]
        else:
          self.cols[col].append(self.spaces[space])
      
      nsr = {}
      for row in self.rows.keys():
​
        r = Array.ROC(self.rows[row])
        nsr[row] = r
      
      nsc = {}
      for col in self.cols.keys():
        c = Array.ROC(self.cols[col])
        nsc[col] = c
​
      self.rows = nsr
      self.cols = nsc
      del nsr
      del nsc
​
    def box_size(self, start):
      size = 0
      row_size = 0
​
      row = start[0]
      col = int(start[1])
      new_cols = []
​
      odd = self.spaces[start].odd
      
      while odd == True:
        row_size += 1
        col += 1
        new_cols.append(col)
        try:
          odd = self.spaces['{}{}'.format(row, col)].odd
        except KeyError:
          odd = False
      
      if row_size == 0:
        return 0
      
      col_size = 0
      a = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
      max_row = max(list(self.rows.keys()))
      r_index = a.index(row)
      odd = self.spaces[start].odd
      col = int(start[1])
      new_rows = []
​
      while odd == True:
        r_index += 1
        row = a[r_index]
        col_size += 1
        new_rows.append(row)
        try:
          odd = self.spaces['{}{}'.format(row, col)].odd
        except KeyError:
          odd = False
      #print(row_size, col_size)
      if row_size == col_size:
       # print('yo', row_size)
        return row_size
      elif col_size > row_size:
        count = 0
        for row in new_rows:
          broken = False
          for col in new_cols:
            try:
              if self.spaces['{}{}'.format(row, col)].odd == False:
                broken = True
                break
            except KeyError:
              pass
          if broken == True:
            if count < row_size:
              return count
            else:
              return row_size
          else:
            count += 1
        return row_size
      else:
        #print('hi', min([row_size, col_size]))
        return min([row_size, col_size])
​
​
  A = Array(lst)
​
  box_sizes = [A.box_size(a) for a in A.spaces.keys()]
  #print(box_sizes)
  try:
    return max(box_sizes)
  except ValueError:
    return 0

