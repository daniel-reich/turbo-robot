"""


You are given a list which may contain sublists. Your task is to find the
depth of the deepest sublist.

  * `[a]` = 1 depth
  * `[[a]]` = 2 depth
  * `[[[a]]]` = 3 depth, etc

### Examples

    deepest([1, [2, 3], 4, [5, 6]]) ➞ 2
    
    deepest([[[[[[[[[[1]]]]]]]]]]) ➞ 10
    
    deepest([1, 4, [1, 4, [1, 4, [1, 4, [5]]]]]) ➞ 5

### Notes

N/A

"""

def deepest(lst):
  count=0
  maxi=0
  print(str(lst))
  for i in range(len(str(lst))):
    if(str(lst)[i]=='['):
      count+=1
      if(count>maxi):
        maxi=count
    if(str(lst)[i]==']'):
      count-=1
    print(count)
  return(maxi)

