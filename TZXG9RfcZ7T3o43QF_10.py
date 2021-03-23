"""


Write a function that returns `True` if every consecutive sequence of **ones**
is followed by a consecutive sequence of **zeroes** of the same length.

### Examples

    same_length("110011100010") ➞ True
    
    same_length("101010110") ➞ False
    
    same_length("111100001100") ➞ True
    
    same_length("111") ➞ False

### Notes

N/A

"""

def same_length(txt):
    one_count = 0
    zero_count = 0
    len_check = True
    txt_list = list(txt)
    for i in range(0,len(txt_list)):
        if txt_list[i] != txt_list[abs(i-1)] and txt_list[i] == '1' and zero_count != one_count:
            len_check = False
            one_count = 0
            zero_count = 0
        if txt_list[i] == '1':
            one_count += 1
        if txt_list[i] == '0':
            zero_count += 1
        if i == (len(txt_list)-1) and zero_count != one_count:
            len_check = False
    return len_check

