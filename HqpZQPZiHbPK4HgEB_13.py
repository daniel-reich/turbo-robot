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
  s=str(n)
  maxx,minn, lst=n,n,[]
  for i in range (len(s)):
    for j in range(1,len(s)):
      out=list(s)
      out[j],out[i]=s[i],s[j]
      lst.append(int(''.join(out)))
  lst1 = [i for i in lst if i > 10**(len(s)-1)]
  return (max(lst1),min(lst1))

