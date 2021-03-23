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
  
  
  def test(w,a,b,ll):
    if a<0 or b<0 or a>=len(grid) or b>=len(grid[0]) or (a,b) in ll: return []
    if grid[a][b]!=w[0]: return []
​
    if len(w)<2: return [(a,b)]
    
    for i in range(4):
      if i==0:
        tmp=test(w[1:],a-1,b,ll+[(a,b)])
      elif i==1:
        tmp=test(w[1:],a+1,b,ll+[(a,b)])
      elif i==2:
        tmp=test(w[1:],a,b-1,ll+[(a,b)])
      else:
        tmp=test(w[1:],a,b+1,ll+[(a,b)])
      if len(tmp)==len(w)-1:
        return [(a,b)]+tmp
    return []
      
​
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      tmp=test(word,i,j,[])
      print('*',i,j,tmp)
      if len(tmp)==len(word):
        return tmp
  return 'Not present'

