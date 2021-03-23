"""


Create a function which counts how many lone `1`s appear in a given number.
Lone means the number doesn't appear twice or more in a row.

### Examples

    count_lone_ones(101) ➞ 2
    
    count_lone_ones(1191) ➞ 1
    
    count_lone_ones(1111) ➞ 0
    
    count_lone_ones(462) ➞ 0

### Notes

Tests will include positive whole numbers only.

"""

def count_lone_ones(n):
  x=str(n)
  a=[]
  count=0
  for i in x:
    a.append(int(i))
  a.append(0)
  for i in range(len(a)-1):
    if a[i]==1 and a[i+1]!=1 and a[i-1]!=1:
      count+=1
  return(count)

