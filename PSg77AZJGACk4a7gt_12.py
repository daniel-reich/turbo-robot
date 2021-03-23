"""


For this challenge, forget how to add two numbers together. The best
explanation on what to do for this function is this meme:

![Alternative Text](https://edabit-challenges.s3.amazonaws.com/caf.jpg)

### Examples

    meme_sum(26, 39) ➞ 515
    # 2+3 = 5, 6+9 = 15
    # 26 + 39 = 515
    
    meme_sum(122, 81) ➞ 1103
    # 1+0 = 1, 2+8 = 10, 2+1 = 3
    # 122 + 81 = 1103
    
    meme_sum(1222, 30277) ➞ 31499

### Notes

N/A

"""

def meme_sum(a, b):
  sa, sb = str(a), str(b)
  if len(sa) > len(sb):
    sb = '0' * (len(sa) - len(sb)) + sb
  elif len(sb) > len(sa):
    sa = '0' * (len(sb) - len(sa)) + sa
  res = ''
  for i, j in zip(sa, sb):
    res += str(int(i) + int(j))
  return int(res)

