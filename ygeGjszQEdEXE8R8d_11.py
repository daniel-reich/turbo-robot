"""


Create a function which takes a parameter `mat`, where `mat` is a matrix
(`list` of `list`s) such that all but one entry equals `0` (and the non-zero
entry equals `1`). The function, after being passed a matrix, should be
repeatedly callable with the following `str` commands:

  * `"up"` ➞ Move the `1` to the cell above it.
  * `"down"` ➞ Move the `1` to the cell below it.
  * `"left"` ➞ Move the `1` to the cell to the left of it.
  * `"right"` ➞ Move the `1` to the cell to the right of it.
  * `"stop"` ➞ Return the resulting matrix.

### Examples

    one = [
      [1]
    ]
    
    two = [
      [1, 0],
      [0, 0]
    ]
    
    # Should work for 1×1 matrices
    move(one)("up")("stop") ➞ [
      [1]
    ]
    
    # The 1 should wrap around
    move(two)("left")("stop") ➞ [
      [0, 1],
      [0, 0]
    ]
    
    # Should accept multiple commands
    move(two)("right")("down")("stop") ➞ [
      [0, 0],
      [0, 1]
    ]
    
    # Should return a function
    callable(move(two)) ➞ True

### Notes

  * The matrix can be of any size `m×n`, where `m ≥ 1` and `n ≥ 1`.
  * The `1` should be able to wrap around, e.g. if the non-zero entry is at the top of the matrix, calling the command `'up'` should move it to the bottom of the matrix.
  * The result of the original function `move` should be callable an arbitrary number of times.

"""

def move(mat):
  closure  = lambda command : helper(mat , command) if command == "stop" else move(helper(mat , command));  
  return closure ;
​
def helper(mat , command):
  if (command == "stop"):
    return mat;
    
  (rows , columns)  = (len(mat) , len(mat[0]));
  one_idx  = getIndex(mat,1);
  commandsToDirection  = {
    "up" : (0,-1) ,
    "down" : (0,1) , 
    "left" : (-1,0) , 
    "right" : (1,0)
    };
    
  one_row  = (one_idx["row"] + commandsToDirection[command][1]) % rows;
  one_column = (one_idx["column"] +  commandsToDirection[command][0]) % columns;
  
  return matrix(rows , columns ,  one_column, one_row );
​
def getIndex(lst , value ):
  for k in range(0, len(lst)):
    row  = lst[k];
    try :
      return dict(row =  k , column = row.index(1))
    except ValueError:
      pass;
  raise ValueError("couldn't find searched value anyway..");

