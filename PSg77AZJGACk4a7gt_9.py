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
  x = str(a) if len(str(a)) >= len(str(b)) else '0'*(len(str(b)) - len(str(a))) + str(a) 
  y = str(b) if len(str(b)) >= len(str(a)) else '0'*(len(str(a)) - len(str(b))) + str(b)
  z = ''.join(str(int(x[i]) + int(y[i])) for i in range(len(x)))
  return int(z)

