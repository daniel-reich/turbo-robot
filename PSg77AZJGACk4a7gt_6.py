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
  sum = ""
  c=0
  if b>a:
      c=a
      a=b
      b=c
  a = str(a)
  b= str(b)  
  i=0
  while i < (len(a)-len(b)):
    sum = sum + a[i]
    i += 1
  i = 0
  while i < len(b):
    sum = sum + str((int(a[i+len(a)-len(b)])+ int(b[i])))
    i += 1
  return int(sum)

