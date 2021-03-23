"""


A number `n` is **apocalyptic** if 2^n contains a string of 3 consecutive 6s
(666 being the presumptive "number of the beast").

Create a function that takes a number `n` as input. If the number is
apocalyptic, find the index of 666 in 2^n, and return `"Repent! X days until
the Apocalypse!"` (X being the index). If not, return `"Crisis averted. Resume
sinning."`.

### Examples

    apocalyptic(109) ➞ "Crisis averted. Resume sinning."
    
    apocalyptic(157) ➞ "Repent! 9 days until the Apocalypse!"
    # 2^157 -> 182687704666362864775460604089535377456991567872
    # 666 at 10th position (index 9)
    
    apocalyptic(175) ➞ "Crisis averted. Resume sinning."
    
    apocalyptic(220) ➞ "Repent! 6 days until the Apocalypse!"

### Notes

N/A

"""

def apocalyptic(n):
  n = str(2**n)
  count = 0
  for i in range(0, len(n), 1):
    if n[i]=='6':
      count=count+1
      if count == 3:
        return 'Repent! ' + str(i-2) + ' days until the Apocalypse!'
    else:
      count = 0
  return 'Crisis averted. Resume sinning.'

