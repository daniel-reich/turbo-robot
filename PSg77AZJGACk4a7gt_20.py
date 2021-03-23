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
  m = str(a)
  n = str(b)
  l = abs(len(m)-len(n))
  if len(m)<len(n):
    m1 = l*'0'+ m
    lst1 = [int(i) for i in m1]
    lst2 = [int(i) for i in n]
    return int(''.join([str(i+j) for i,j in zip(lst1,lst2)]))
  else:
    n1 = l*'0'+ n
    lst1 = [int(i) for i in n1]
    lst2 = [int(i) for i in m]
    return int(''.join([str(i+j) for i,j in zip(lst1,lst2)]))

