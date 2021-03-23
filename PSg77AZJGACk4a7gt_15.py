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
  if len(str(a)) < len(str(b)):
    number_one = str(a)
    number_two = str(b)
    number_three = ''
    while len(number_one) < len(number_two):
      number_one = '0' + number_one
    for i in range(len(number_one)):
      number_three += str(int(number_one[i]) + int(number_two[i]))
    return int(number_three)
  else:
    number_one = str(a)
    number_two = str(b)
    number_three = ''
    while len(number_two) < len(number_one):
      number_two = '0' + number_two
    for i in range(len(number_two)):
      number_three += str(int(number_one[i]) + int(number_two[i]))
    return int(number_three)

