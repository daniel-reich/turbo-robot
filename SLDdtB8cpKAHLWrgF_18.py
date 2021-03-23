"""


In this challenge, you have to permutate an expression that includes three
variable values `a`, `b` and `c`. You are given a set of three unique numbers
to substitute for letters so there are six possible different expression
variations, and you have to find which one returns the greater result.

    expr = "(a - b) * c" | nums = [1, 2, 3]
    
    Permutation #1 ➞ (1 - 2) * 3 = -3
    Permutation #2 ➞ (1 - 3) * 2 = -4
    Permutation #3 ➞ (2 - 1) * 3 = 3
    Permutation #4 ➞ (2 - 3) * 1 = -1
    Permutation #5 ➞ (3 - 1) * 2 = 4
    Permutation #6 ➞ (3 - 2) * 1 = 1
    
    # Permutation #5 returns the greater result.

Given an expression string `expr` and a list of three numbers `nums`, the
function must return a string with the complete notation of the expression
that returns the greater result (adding the equal sign after the expression
and the result after the equal sign). For the example above, the result will
be:

    greater_permutation("(a - b) * c", [1, 2, 3]) ➞ "(3 - 1) * 2 = 4"

If an expression returns a float number as result, round it to the nearest
hundredth.

### Examples

    greater_permutation("(a - b) * c", [1, 2, 3]) ➞ "(3 - 1) * 2 = 4"
    
    greater_permutation("a ** b - c", [2, 3, 1]) ➞ "3 ** 2 - 1 = 8"
    
    greater_permutation("a % b + (c * 2)", [3, 1, 2]) ➞ "1 % 2 + (3 * 2) = 7"

### Notes

  * Every given expression is designed to have just one permutation that returns a maximum result, don't worry about multiple matches.
  * Expressions can contain known values besides the three variables (see example #3).
  * Remember to round to the nearest hundredth if the result is a float number.

"""

import re
def greater_permutation(express, num_list):
    permutaions = []
    length = 3
    max_result = 0
    result_str = ""
    for i in range(3):
        ele = []
        temp1 = num_list.copy()
        first = temp1.pop(i)
        for j in range(2):
            temp2 = temp1.copy()
            second = temp2.pop(j)
            ele = [first, second, temp2[0]]
            permutaions.append(ele)
    
    for ele in permutaions:
        temp_express = re.sub('a', str(ele[0]),express)
        temp_express = re.sub('b', str(ele[1]),temp_express)
        temp_express = re.sub('c', str(ele[2]),temp_express)
        
        temp_result = eval(temp_express)
        if temp_result >= max_result:
            max_result = temp_result
            max_result = round(max_result,2)
            if max_result == 0:
                max_result = int(0)
            result_str = temp_express + " = " + str(max_result)
    result_str = result_str.rstrip('0').rstrip('.') if '.' in result_str else result_str
    return result_str

