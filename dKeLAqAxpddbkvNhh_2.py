"""


A group of `n` friends are going to see a movie. They would like to find a
spot where they can sit next to each other in the same row. A movie theater's
seat layout can be represented as a 2-D matrix, where `0`s represent empty
seats and `1`s represent taken seats.

    [[1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0]]

Create a function that, given a seat layout and the number of friends `n`,
returns the number of available spots for all `n` friends to sit together. In
the above example, if `n = 3`, there would be 2 spots (the first row and last
row).

### Examples

    group_seats([
      [1, 0, 1, 0, 1, 0, 1],
      [0, 1, 0, 1, 0, 1, 0],
      [0, 0, 1, 1, 1, 1, 1],
      [1, 0, 1, 1, 0, 0, 1],
      [1, 1, 1, 0, 1, 0, 1],
      [0, 1, 1, 1, 1, 0, 0]
    ], 2) ➞ 3
    
    group_seats([
      [1, 0, 1, 0, 1, 0, 1],
      [0, 1, 0, 0, 0, 0, 0],
    ], 4) ➞ 2

### Notes

Multiple free arrangements that overlap still count as distinct arrangements
(see example #2).

"""

def group_seats(lst, n):
  f=0
  for i in lst:
    
    for c in range(len(i)):
      a=c
      count=0 
      if i[a]==0 : 
        while i[a]==0 :
          a=a+1
          if count<n: count=count+1
          if a==len(i): break
          
                    
                        
      if count==n: 
          f=f+1
          print(i)
            
      
  
  return f

