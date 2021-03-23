"""


Write a function that returns `True` if a string consists of **ascending or
ascending AND consecutive** numbers.

### Examples

    ascending("232425") ➞ True
    # Consecutive numbers 23, 24, 25
    
    ascending("2324256") ➞ False
    # No matter how this string is divided, the numbers are not consecutive.
    
    ascending("444445") ➞ True
    # Consecutive numbers 444 and 445.

### Notes

A **number** can consist of any number of digits, so long as the numbers are
adjacent to each other, and the string has at least two of them.

"""

def ascending(st):
    for sub_len in range(1,len(st)//2+1):
        if len(st) % sub_len != 0: continue
        num_of_sub_nums = len(st) // sub_len
        nums = [int(st[i*sub_len:(i+1)*sub_len]) for i in range(num_of_sub_nums)]
        min_ = min(nums)
        if list(map(lambda x:x-min_,nums)) == list(range(num_of_sub_nums)): return True
    return False

