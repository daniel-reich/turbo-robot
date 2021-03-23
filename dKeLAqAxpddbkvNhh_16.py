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
 count=0
 #go through rows
 for i in range(0,len(lst)):
  # print('i',i)
  #find 0 in row i
  for k in range(0,len(lst[i])-n+1):
   # print('k',k)
   # print(lst[i][k])
   if lst[i][k] == 0:
   # if n-1 0's follow
    follow=True
    for p in range(1,n):
     # print('p',p)
     # print('lst[i][(k+p)]',lst[i][(k+p)])
     if lst[i][(k+p)] == 0:
      continue
     else:
      follow=False
      break
    # print('follow',follow)
    if follow:
     count+=1
    # print('count',count)
   
 return count

