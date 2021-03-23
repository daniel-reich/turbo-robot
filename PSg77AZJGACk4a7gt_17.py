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
    str_a = str(a)
    str_b = str(b)
    len_a = len(str(a))
    len_b = len(str(b))
    difflen = abs(len_a-len_b)
​
    str_a_rev = ""
    str_b_rev = ""
​
    for i in range(len_a):
        str_a_rev = str_a[i] + str_a_rev 
    for i in range(len_b):
        str_b_rev = str_b[i] + str_b_rev    
        
    if len_a > len_b:
        str_b_rev = str_b_rev + '0'*(difflen)
    elif len_a < len_b:
        str_a_rev = str_a_rev + '0'*(difflen)
​
    answer = ''
    for i in range(max(len_a,len_b)):
        answer = str(int(str_a_rev[i])+int(str_b_rev[i]))+answer
  
    return int(answer)

