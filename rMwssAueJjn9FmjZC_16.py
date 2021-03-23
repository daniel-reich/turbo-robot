"""


Create a function that determines how many number pairs are there embedded in
a space-separated string. The first numeric value in the space-separated
string represents the count of the numbers, thus, excluded in the pairings.

### Examples

    number_pairs("7 1 2 1 2 1 3 2") ➞ 2
    # (1, 1), (2, 2)
    
    number_pairs("9 10 20 20 10 10 30 50 10 20") ➞ 3
    # (10, 10), (20, 20), (10, 10)
    
    number_pairs("4 2 3 4 1") ➞ 0
    # although two 4's are present but
    # the first one is discounted

### Notes

Always take into consideration the first number in the string is not part of
the pairing, thus, the count. It may not seem so useful as most people see it,
but it's mathematically significant if you deal with **set operations**.

"""

def number_pairs(txt):
  number = int(txt.split(' ')[0])
  rest = txt.split(' ')[1:]
  newlist = sorted(list([int(x) for x in rest]))
  newlist2 = []
  for eachnumber in newlist:
    if newlist.count(eachnumber) > 1:
      newlist2.append(1)
      x = newlist.index(eachnumber)
      del newlist[x]
      x = newlist.index(eachnumber)
      del newlist[x]
  for eachnumber in newlist:
    if newlist.count(eachnumber) > 1:
      newlist2.append(1)
      x = newlist.index(eachnumber)
      del newlist[x]
      x = newlist.index(eachnumber)
      del newlist[x]
  return sum(newlist2)
