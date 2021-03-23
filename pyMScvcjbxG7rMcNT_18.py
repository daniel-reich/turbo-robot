"""


Create a function that takes a list and returns the sum of all the items in
that list.

### Examples

    sum_list([1, 2, 3]) ➞ 6
    # 1 + 2 + 3 = 6
    
    sum_list([1, [2, [1]], 3]) ➞ 7
    # 1 + 2 + 1 + 3 = 7

### Notes

  * An item in the list can be another list.
  * Try solving it in a recursive approach without using the built-in `sum()` function.

"""

def sum_list(nums):
    out = 0
    for num in nums:
        if type(num) == list:
            for n in num:
                if type(n) == list:
                    for i in n:
                        out += i
                else:
                    out += n
        else:
            out += num
    return out

