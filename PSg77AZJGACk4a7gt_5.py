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
    a_str, b_str = str(a), str(b)
    width = len(a_str) if len(a_str) > len(b_str) else len(b_str)
    a_str, b_str = a_str.zfill(width), b_str.zfill(width)
    sum_str = ''.join(str(int(dd[0]) + int(dd[1])) for dd in zip(a_str, b_str))
    return int(sum_str)

