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

def maxmin(nn):
  nn=str(nn)
  n=list()
  for i in nn:
    n.append(i)
  result=list()
  result.append(int(nn))
  for i in range(0,len(n)):
    for j in range(i+1,len(n)):
      m=list()
      m.extend(n)
      x=m[j]
      m[j]=m[i]
      m[i]=x
      print(m)
      if(m[0]!='0'):
        result.append(int(''.join(m)))
      
  return (max(result),min(result))

