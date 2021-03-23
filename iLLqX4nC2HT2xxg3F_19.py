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
  s=""
  c=1
  i=[]
  switch=True
  for t in lst:
    s=s+str(t)
  for r in s:
    if r=="[":
      c+=1
      switch=True
    elif r=="]":
      if switch==True:
        switch=False
        i.append(c)
        c-=1
      else:
        c-=1
  if len(i)==0:
    return 1
  else:
    return max(i)

