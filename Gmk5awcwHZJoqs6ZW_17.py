"""


An **island is a region of contiguous ones**. A contiguous one is a `1` that
is touched by at least one other `1`, either **horizontally** , **vertically**
or **diagonally**. Given a piece of the map, represented by a 2-D list, create
a function that returns the area of the largest island.

To illustrate, if we were given the following piece of the map, we should
return `4`.

    [
      [0, 0, 0],
      [0, 1, 1],
      [0, 1, 1]
    ]

Our function should yield `2` for the map below:

    [
      [1, 0, 0],
      [0, 0, 1],
      [0, 0, 1]
    ]

Our function should yield `4` for the map below: :

    [
      [1, 0, 0],
      [0, 1, 1],
      [0, 0, 1]
    ]

### Examples

    largest_island([
      [1, 0, 0], 
      [0, 0, 0], 
      [0, 0, 1]
    ])
    
    ➞ 1
    
    largest_island([
      [1, 1, 0], 
      [0, 1, 1], 
      [0, 0, 1]
    ])
    
    ➞ 5
    
    largest_island([
      [1, 0, 0], 
      [1, 0, 0], 
      [1, 0, 1]
    ])
    
    ➞ 3

### Notes

  * Maps can be any `m x n` dimension.
  * Maps will always have at least 1 element. `m >= 1` and `n >= 1`.

"""

def checkNeighbors(lst, i, j):
  part_sum = 0; n_01 = 0; n_10 = 0; n_11 = 0; n_00 = 0; n_22 = 0;
  j_length = len(lst[0])-1;
  i_length = len(lst)-1;
  if ((j < j_length) and (i > 0)):
    n_22 = lst[i-1][j+1];
  if ((j > 0) and (i < i_length)):
    n_00 = lst[i+1][j-1];
  if (j < j_length):
    n_01 = lst[i][j+1];
    if (i < i_length):
      n_11 = lst[i+1][j+1];
  if (i < i_length):
    n_10 = lst[i+1][j];
    
  part_sum = n_00 + n_01 + n_11 + n_10 + n_22;
  
  if (n_11 == 1):
    return (part_sum, i+1, j+1);
  elif (n_10 == 1):
    return (part_sum, i+1, j);
  elif (n_01 == 1):
    return (part_sum, i, j+1);
  elif (n_00 == 1):
    return (part_sum, i+1, j-1);
  elif (n_22 == 1):
    return (part_sum, i-1, j+1);
  else:
    return (part_sum, i+1 , j+1);
​
def largest_island(lst):
  print (lst);
  largest = 0;
  curr = 0;
  first_one = 1;
  m = len(lst);
  n = len(lst[0]);
  p_sum = 1;
  for i in range(m):
    for j in range(n):
      if ((lst[i][j] == 1) or (p_sum == 0)):
        if (first_one):
          curr += 1;
          first_one = 0;
        (p_sum, new_i, new_j) = checkNeighbors(lst,i,j); 
        i = new_i;
        j = new_j;        
        if (p_sum == 0):
          if (curr > largest):
            largest = curr;
          curr = 0;
        else:
          curr += p_sum;
        print (p_sum, new_i, new_j, curr,largest);
        if ((i == m-1) or (j == n-1)):
          if (curr > largest):
            largest = curr;
          return largest;
  return largest;

