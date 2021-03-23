"""


Create a function that takes an integer list and return the biggest between
**positive** sum, **negative** sum, or **0s** count. The major is understood
as the greatest absolute.

`l = [1,2,3,4,0,0,-3,-2]`, the function has to return `10`, because:

  * Positive sum = 1+2+3+4 = 10
  * Negative sum = (-3)+(-2) = -5
  * 0s count = 2 (there are two zeros in list)

### Examples

    major_sum([1, 2, 3, 4, 0, 0, -3, -2]) ➞ 10
    
    major_sum([-4, -8, -12, -3, 4, 7, 1, 3, 0, 0, 0, 0]) ➞ -27
    
    major_sum([0, 0, 0, 0, 0, 1, 2, -3]) ➞ 5
    # Because -3 < 1+2 < 0sCount = 5

### Notes

  * All numbers are integers.
  * There aren't empty lists.
  * All tests are made to return only one value.

"""

def major_sum(lst):
    pos_num = 0
    neg_num = 0
    zeroes = 0
    i = 0
    result_nums = []
    for i in range(len(lst)):
        if lst[i] > 0:
            pos_num += lst[i]
        elif lst[i] < 0:
            neg_num += lst[i]
        else:
            zeroes += 1
​
    
    print(zeroes)
    print(pos_num)
    print(neg_num)
    if pos_num > abs(neg_num) >= zeroes:
        return pos_num
    elif pos_num > zeroes >= abs(neg_num):
        return pos_num
    elif zeroes > pos_num >= abs(neg_num):
        return zeroes
    elif zeroes > abs(neg_num) >= pos_num:
        return zeores
    elif abs(neg_num) > zeroes >= pos_num:
        return neg_num
    elif abs(neg_num) > pos_num >= zeroes:
        return neg_num

