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
    s_a, s_b = str(a), str(b)
    len_a, len_b = len(s_a), len(s_b)
    max_len = max(len_a, len_b)
    lst_a = [0] * (max_len - len_a) + list(map(int, list(s_a)))
    lst_b = [0] * (max_len - len_b) + list(map(int, list(s_b)))
    return int("".join(str(i + j) for i, j in zip(lst_a, lst_b)))

