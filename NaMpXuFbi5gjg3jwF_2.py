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
 sock_set=set(socks)
 #print(sock_set)
 pairs=0
 for sock in sock_set:
  count=0
  for i in range(0,len(socks)):
   if socks[i] == sock:
    count+=1
  if count // 2 > 0:
   pairs+=int(count//2)
 return pairs

