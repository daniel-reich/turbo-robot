"""


Maxie is the largest number that can be obtained by **swapping two digits** ,
Minnie is the smallest. Write a function that takes a number and returns Maxie
and Minnie. Leading zeros are not permitted.

### Examples

    maxmin(12340) ➞ (42310, 10342)
    
    maxmin(98761) ➞ (98761, 18769)
    
    maxmin(9000) ➞ (9000, 9000)
    # Sometimes no swap needed.
    
    maxmin(11321) ➞ (31121, 11123)

### Notes

N/A

"""

def maxmin(n):
  lst = [n]
  n = str(n)
  for i in range(len(n)):
    for j in range(i+1,len(n)):
      temp = list(n)
      temp[i],temp[j] = temp[j],temp[i]
      if temp[0]!='0' and int(''.join(temp)) not in lst:
        lst.append(int(''.join(temp)))
  return (max(lst),min(lst))

