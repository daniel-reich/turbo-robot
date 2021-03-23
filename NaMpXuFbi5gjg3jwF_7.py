"""


Joseph is in the middle of packing for a vacation. He's having a bit of
trouble finding all of his socks, though.

Write a function that returns the number of sock pairs he has. A sock pair
consists of two of the same letter, such as `"AA"`. The socks are represented
as an unordered sequence.

### Examples

    sock_pairs("AA") ➞ 1
    
    sock_pairs("ABABC") ➞ 2
    
    sock_pairs("CABBACCC") ➞ 4

### Notes

  * If given an empty string (no socks in the drawer), return `0`.
  * There can be multiple pairs of the same type of sock, such as two pairs of `CC` for the last example.

"""

def sock_pairs(socks):
  pairs=0
  nn=0
  for i in socks:
    if socks.index(i,nn)==0:
      pairs=pairs+socks.count(i)/2-.5*(socks.count(i)%2)
    else:
      if socks.index(i,0)==socks.index(i,nn):
        pairs=pairs+socks.count(i)/2-.5*(socks.count(i)%2)
    nn+=1
  return pairs

