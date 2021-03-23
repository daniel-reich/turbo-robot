"""


Create a function that produces a random number that contains all numbers from
one to five, without any duplicates.

### Examples

    12345
    
    21345
    
    51234

### Notes

N/A

"""

from datetime import datetime
def numbers():
  ans=''
  while len(ans)<5:
    a=int(str(datetime.now().microsecond)[-1])
    if a>0 and a<6 and str(a) not in ans: ans+=str(a)
  return int(ans)

