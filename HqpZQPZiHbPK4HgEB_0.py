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
  swaps, n = [n], str(n)
  for a in range(len(n)):
    for b in range(len(n)):
      if a != b:
        swap = list(n)
        swap[a], swap[b] = swap[b], swap[a]
        if swap[0] != '0':
          swaps.append(int(''.join(swap)))
  return (max(swaps), min(swaps))

