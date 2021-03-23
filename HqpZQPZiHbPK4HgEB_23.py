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

def maxmin(no):
   lst=[i for i in str(no)]
   lst1=lst.copy()
   finallst=[no]
   for k in range(len(lst)):
    for n in range(1,len(lst)):
     lst1[k], lst1[n] = lst1[n], lst1[k]
     if len(str(int("".join(lst1)))) == len(lst):
       finallst.append(int("".join(lst1)))
     lst1 = lst.copy()
​
​
   return(max(finallst),min(finallst))

