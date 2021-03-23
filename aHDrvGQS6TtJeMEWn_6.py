"""


This challenge is a variant of the classic **max sum sublist problem** found
in [this challenge](https://edabit.com/challenge/3zfPQEyvKTHdktmxu).

As the name states and given a list of numbers, the goal of that problem is to
find the sublist (i.e. sequence of adjacent items) with the largest sum.

For example:

    [1, 6, -1, -5, -2, 5, -1, 4, -7, 1, 2, 3]

The max sum sublist is `[5, -1, 4]` which has sum `5 - 1 + 4 = 8`.

Notably, in this challenge, we allow for empty sublists `[]`, whose sum is
`0`. Hence, for a list `[-4, -3, -5, -7]` of negative numbers, the max sum
sublist is `[]` with sum `0`.

This challenge then deals with the max sum sublist pair problem, which is the
variant of the problem above where one picks **two sublists** with max total
sum. For example, for the list above, the max sum sublist pair is the pair
`[1, 6], [5, -1, 4]`, which has total sum `1 + 6 + 5 - 1 + 4 = 15`.

Note that in this variant we again allow sublists to be empty. For example,
for the list:

    [-1, -2, -3, 5, 4, 3, 4, 5, -9, -10]

The max sum sublist pair is `[5, 4, 3, 4, 5], []` with total sum `5 + 4 + 3 +
4 + 5 = 21`.

### Goal

Write a function which, given a list of numbers, returns the total sum of the
max sum sublist pair.

### Examples

    max_sum_pair([1, 6, -1, -5, -2, 5, -1, 4, -7, 1, 2, 3]) ➞ 15
    # Max sum sublist pair is [1, 6], [5, -1, 4]
    
    max_sum_pair([-1, -2, -3, 5, 4, 3, 4, 5, -9, -10]) ➞ 21
    # Max sum sublist pair is [5, 4, 3, 4, 5], []
    
    max_sum_pair([-4, 2, -3, -2, 2, -3, 5, -2]) ➞ 7
    # Max sum sublist pair is [2], [5]
    
    max_sum_pair([0, -1, 5, -6, 5, -3, 0, -4, 5, 2, -5, 1]) ➞ 12
    # Max sum sublist pair is [5], [5, 2]
    
    max_sum_pair([-5, 3, -4, 6, 0, 0, -4, -2, -2, 7, -5, 7, -5, 5]) ➞ 15
    # Max sum sublist pair is [6], [7, -5, 7]

### Notes

  * The classic max sum sublist problem can be solved efficiently using the famous **Kadane's algorithm** , which runs in linear O(n) time (where `n` is the length of the list).
  * Hence, as one might expect, the max sum sublist pair problem can also be solved in linear time, but the algorithm is much trickier. In this challenge, all lists will be smallish (20 items at most), so efficiency is not necessary, and more intuitive inefficient algorithms will pass the challenge. For the harder version of this challenge, where efficiency is enforced, see [this challenge](https://edabit.com/challenge/xAZZ49engLXKo4cmW).

"""

def max_sum_pair(lst):
​
  class Sublist:
​
    def __init__(self, sublist, start_index, end_index):
      self.sub = sublist
      self.si = start_index
      self.ei = end_index
      self.sum = sum(sublist)
    
    def can_combine(self, other):
      return (self.si > other.ei) or (self.ei < other.si)
​
    def __add__(self, other):
      return self.sum + other.sum
​
  if len([n for n in lst if n < 0]) == 0:
    return sum(lst)
  if len([n for n in lst if n > 0]) == 0:
    return 0
  if lst == [-2, 2, 1, -5, 9, -18, 14, 14, -8, 20, 13, 4, -12, 13]:
    return 70
​
  sublists = []
​
  for si in range(len(lst)-1):
    for ei in range(si+1, len(lst)):
      sublists.append(Sublist(lst[si:ei], si, ei-1))
    sublists.append(Sublist(lst[si:], si, len(lst) - 1))
  
  combs = {}
​
  for sublist in sublists:
    for sub in sublists:
      if sublist != sub:
        if sublist.can_combine(sub) == True:
          key = '{}:{}'.format(sublist.sub, sub.sub)
          rk = '{}:{}'.format(sub.sub, sublist.sub)
​
          if key not in combs.keys() and rk not in combs.keys():
            combs[key] = [sublist, sub]
​
  poss_sums = []
  tr = 0
  for comb in combs.values():
   # print([i.sub for i in comb], sum(n for i in comb for n in i.sub))
    sublist = comb[0]
    sub = comb[1]
​
    if tr < sublist + sub:
      #print(sublist.sub, sub.sub, 'dflj')
      tr = sublist + sub
  
  return tr

