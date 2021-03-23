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
  largest=0
  if lst==[[]]:
    return largest
  num_rows= len(lst)
  if len(lst)>1:
    num_columns = len(lst[0])
  else:
    num_columns=0
  for m in range (1,max(min(num_rows,num_columns)+1,2)):
    for j in range (num_rows-m+1):
      for k in range(max(num_columns-m+1,1)):
        tmp=[row[k:k+m] for row in lst[j:j+m]]
        counter, counter_odd =0,0
        for n in range(len(tmp)):
          if(len(tmp)>1):
            for o in range(len(tmp[0])):
              counter+=1
              if (tmp[n][o]%2==1):
                counter_odd+=1
          else:
            for o in range(len(tmp)):
              if (tmp[o][0]%2==1):
                largest=m
                break
        if (counter == counter_odd and len(tmp)>1):
          largest = m
  return(largest)

