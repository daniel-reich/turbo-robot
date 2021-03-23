"""


This is a **reverse coding challenge**. Normally you're given explicit
directions with how to create a function. Here, you must generate your own
function to satisfy the relationship between the inputs and outputs.

Your task is to create a function that, when fed the inputs below, produce the
sample outputs shown.

### Examples

    3 ➞ 21
    
    9 ➞ 2221
    
    17 ➞ 22221
    
    24 ➞ 22228

### Notes

If you get stuck, check the **Comments** for help.

"""

def mystery_func(num):
    test_num = 2
    remainder = 0
    num_of_twos = 1
    n = 1
    final_number = 0
    while True:
        if num - test_num < test_num:
            remainder = num - test_num
            break
        test_num *= 2
        num_of_twos += 1
    for i in range(num_of_twos):
        final_number += (2 * (10 ** (i + 1)))
    return final_number + remainder

