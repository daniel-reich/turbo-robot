"""


A grid of letters may contain a word hidden somewhere within it. The letters
of the word may be traced from the starting letter by moving a single letter
at a time, up, down, left or right. For example, suppose we are looking for
the word BISCUIT in this grid:

    [
      ["B","I","T","R"],
      ["I","U","A","S"],
      ["S","C","V","W"],
      ["D","O","N","E"]
    ]

The word starts in the top left corner, continues downwards for 2 more
letters, then the letter to the right followed by 2 letters moving upwards,
the final letter at the right of the penultimate one.

Write a function which takes in a target word and a grid of letters and
returns a list of tuples, each tuple being the row and column of the
corresponding letter in the grid (numbered from 0). If the word cannot be
found, output the string "Not present".

### Examples

    trace_word_path("BISCUIT", [
      ["B", "I", "T", "R"],
      ["I", "U", "A", "S"],
      ["S", "C", "V", "W"],
      ["D", "O", "N", "E"]
    ]) ➞ [(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2)]
    
    trace_word_path("HELPFUL", [
      ["L","I","T","R"],
      ["U","U","A","S"],
      ["L","U","P","O"],
      ["E","F","E","H"]
    ]) ➞ "Not present"

### Notes

  * The target word will never be longer than the grid of letters.
  * Target word and the letters grid will be in upper case.

"""

def trace_word_path(word, grid):
  indices = [[] for k in range(len(word))]
  def neighbors(i,j):
    lst = []
    for a,b in zip([i-1,i,i,i+1],[j,j-1,j+1,j]):
      if min(a,b) >= 0 and a < len(grid) and b < len(grid[0]):
        lst.append((a,b))
    return lst
  def letters(i,j):
    return list(map(lambda x: grid[x[0]][x[1]],neighbors(i,j)))
  def is_valid(i,j,k):
    if k > 0 and not word[k-1] in letters(i,j):
        return False
    else:
      try:
        return word[k+1] in letters(i,j)
      except IndexError:
        return True
  #loop through to find valid indices 
  for k in range(len(word)):
    for i in range(len(grid)):
      for j in range (len(grid[0])):
        if grid[i][j] == word[k]:
          if is_valid(i,j,k):
            indices[k].append((i,j))
    if len(indices[k]) == 0:
      return 'Not present'
    elif len(indices[k]) == 1:
      indices[k] = indices[k][0]
  #check for duplicates 
  for k in range(0,len(word)):
    if isinstance(indices[k],list):
      indices[k] = list(filter(lambda x: not x in indices,indices[k]))      
      if len(indices[k]) == 1:
        indices[k] = indices[k][0]
      elif len(indices[k]) == 0:
        return 'Not present'
  #remaining indices
  for k in range(1,len(word)-1):
    if isinstance(indices[k],list):
      if isinstance(indices[k-1],tuple) and isinstance(indices[k+1],tuple):
        if (indices[k-1][0],indices[k+1][1]) in indices[k]:
          indices[k] = (indices[k-1][0],indices[k+1][1])
        elif (indices[k+1][0],indices[k-1][1]) in indices[k]:
          indices[k] = (indices[k+1][0],indices[k-1][1])
        elif indices[k+1][0] == indices[k-1][0]:
          indices[k] = (indices[k+1][0],(indices[k-1][1] + indices[k+1][1])//2)
        elif indices[k+1][1] == indices[k-1][1]:
          indices[k] = ((indices[k-1][0] + indices[k+1][0])//2,indices[k+1][1])
        else:
          return 'Not present'
  #check for duplicates again
  for k in range(0,len(word)):
    if isinstance(indices[k],list):
      indices[k] = list(filter(lambda x: not x in indices,indices[k]))      
      if len(indices[k]) == 1:
        indices[k] = indices[k][0]
      elif len(indices[k]) == 0:
        return 'Not present'
  return indices

