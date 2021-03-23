"""


Write a function that returns the greatest common divisor of all list
elements. If the greatest common divisor is `1`, return `1`.

### Examples

    GCD([10, 20, 40]) ➞ 10
    
    GCD([1, 2, 3, 100]) ➞ 1
    
    GCD([1024, 192, 2048, 512]) ➞ 64

### Notes

  * List elements are always greater than `0`.
  * There is a minimum of two list elements given.

"""

def single_GCD(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return result
​
​
def GCD(lst):
    result_1 = single_GCD(min(lst))
    result_2 = single_GCD(min(lst))
    for ele in lst:
        for num in result_1:
            if ele % num != 0:
                result_2.remove(num)
        result_1 = result_2
    return max(result_1)

