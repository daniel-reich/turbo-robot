"""


For a given list, determine the biggest possible sum between consecutive
terms, as well as the initial and final position of the terms.

### Examples

    big_sub([4, -3, 5, -7, 5]) ➞ [6 (sum), 0 (start), 2 (end)]
    
    big_sub([4, -3, -5, 7, 5]) ➞ [12, 3, 4]
    
    big_sub([2, -3, 2, -3, 2]) ➞ [2, 4, 4]

### Notes

  * If the biggest sum is repeated at several intervals, return the starting and ending positions of the latest interval.
  * The list will always have positive numbers.

"""

def big_sub(lst):
  #print(lst)
  max,out,last=-999,[],-999
  for i,x in enumerate(lst):
    tmp=0
    if x>0 and last<0:
      for j in range(len(lst)-i):
       tmp+=lst[i+j] #sum(lst[i:i+j+1])
       if tmp>=max:max,out=tmp,[i,i+j]
    last=x
    
  return [max]+out

