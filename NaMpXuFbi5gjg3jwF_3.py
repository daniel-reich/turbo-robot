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
    count=0
    for i in set(socks):
        count=count+int(socks.count(i)//2)
    return count

