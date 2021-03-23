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
  larger = a if len(str(a)) >= len(str(b)) else b
  smaller = b if len(str(a)) >= len(str(b)) else a
  res = []
  for i in range(0, len(str(smaller))):
    res.append(int(str(smaller)[len(str(smaller)) - i - 1]) + int(str(larger)[len(str(larger)) - i - 1]))
  for i in range(len(str(larger)) - len(str(smaller)) - 1, -1, -1):
    res.append(int(str(larger)[i]))
  res = res[::-1]
  return int("".join([str(el) for el in res]))

