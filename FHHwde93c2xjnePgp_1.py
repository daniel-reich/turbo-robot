"""


The goal is to test if a consecutive sequence can be formed. A consecutive
sequence is defined as a sequence of incrementing numbers (e.g. 1, 2, 3 or 5,
6, 7, 8). The twist is that you have to consider the combination of lists as
shown. You can combine any two elements from different lists.

    [-5 1 3 5 ] => [3 5 1 -5 ] => [3+4  5+3  1+8  15-5] = [7 8 9 10] => True
    [4 3 8  15] => [4 3 8  15]

Also important is that the lists can be of different sizes, allowing for
partially unpaired numbers in some cases.

    [2 2 2  ] => [2 2 2 0] => [2+5  2+6  2+7  10+0] = [7 8 9 10] => True
    [10 5 6 7] => [5 7 6 10]

### Notes

  * Each list has at least 2 elements.
  * Try the [easier version](https://edabit.com/challenge/uxCqPKsjtxCCqvCZJ).

"""

def has_consecutive_series(lst1, lst2):
  if len(lst1)<len(lst2):return has_consecutive_series(lst2, lst1)
  if len(lst1)>len(lst2):return has_consecutive_series(lst1, lst2 + [0]* (len(lst1)-len(lst2)) )
  s=sum(lst1)+sum(lst2)
  n=max(len(lst1),len(lst2)) # both list have same length
  t=s- (n)*(n-1)//2 # sum(lists) - sum(0..n-1)
  if t%n !=0: return False
  t=t//n # starting value; sum(lists)= sum(t,t+1, ... , t+n-1)
​
  print(s,n,t)
  
  def test(lst1,lst2,t):
    if len(lst1)==0: return True
    for idx,x in enumerate(lst1):
      if (t-x) in lst2:
        tmp=lst2.index(t-x)
        if test(lst1[:idx]+lst1[idx+1:], lst2[:tmp]+lst2[tmp+1:],t+1):
          return True
    return False
  
  return test(lst1,lst2,t)

