"""


Create a function that takes a two-dimensional list as an argument and returns
a one-dimensional list with the values of the original 2d list that are
arranged by spiralling through it (starting from the top-left).

### Examples

    spiral_transposition([
      [7, 2],
      [5, 0]
    ])
    
    ➞ [7, 2, 0, 5]
    
    spiral_transposition([
      [1, 2, 3],  
      [4, 5, 6],
      [7, 8, 9]
    ])
    
    ➞ [1, 2, 3, 6, 9, 8, 7, 4, 5]
    
    spiral_transposition([
      [1, 1, 1],  
      [4, 5, 2],
      [3, 3, 2] 
    ])
    
    ➞ [1, 1, 1, 2, 2, 3, 3, 4, 5]

### Notes

If you do not understand the instructions, write the 3x3 list example on a
piece of paper and trace the output through it.

"""

def spiral_transposition(lst):
  ans=[]
  for i in range(len(lst)):
    ans+=lst[i][i:len(lst[i])-i]
    print(ans)
    if len(ans)==len(lst[0])*len(lst):
      break
    for x in range(i+1,len(lst)-i):
      ans.append(lst[x][-(i+1)])
    print(ans)
    if len(ans)==len(lst[0])*len(lst):
      break
    ans+=(lst[-(i+1)][i:len(lst[i])-1-i])[::-1]
    print(ans)
    if len(ans)==len(lst[0])*len(lst):
      break
    for x in range(len(lst)-i-2,i,-1):
      ans.append(lst[x][i])
    print(ans)
    if len(ans)==len(lst[0])*len(lst):
      break
  return ans

