"""


Many British visitors to edabit will be familiar with Countdown, a quiz
program that ran for many years on UK television. One of its challenges
required contestants to come up with an expression (using some randomly
generated numbers) to meet or get as close as possible to a chosen target
number.

This challenge is a simplified version of that. Write a function that takes in
a tuple of unique positive integers and a target positive integer and returns
a string containing an expression that combines the numbers in the tuple so
that they meet the target, subject to certain rules explained in the notes
below.

### Examples

    countdown((1, 2), 3) ➞ "1+2"
    
    countdown((2, 3, 5, 75), 158) ➞ "3+5+2*75"

### Notes

  * The tuple of operands consists of a minimum of 2 and a maximum of 5 unique positive integers presented in ascending order. An acceptable answer must use each operand once only, combining to meet the target.
  * The operators to use are the standard Python arithmetic operators: `+`, `-`, `*` and `//`. Normal operator precedence rules apply. Do not use parentheses.
  * Each puzzle has at least one answer which meets the above criteria. In the tests, a checker function checks that the expression returned evaluates to the target and that the rules on operands and operators are met.

"""

def permutation_operators_backtracking(cur, lst_operators, result, k):
    if len(cur) == k:
        result.append(cur[:])
    if len(cur) > k:
        return
    else:
        for i in range(len(lst_operators)):
            cur.append(lst_operators[i])
            permutation_operators_backtracking(cur, lst_operators, result, k)
            cur.pop()
    return result
​
​
​
def permutation_operands(cur, lst_operands, used_indexes, result):
    if len(cur) == len(lst_operands):
        result.append(cur[:])
    for i in range(len(lst_operands)):
        if i in used_indexes:
            continue
        cur.append(lst_operands[i])
        used_indexes.append(i)
        permutation_operands(cur, lst_operands, used_indexes, result)
        cur.pop()
        used_indexes.pop()
    return result
​
def string_join(lst_1, str_2):
    result = []
    for i in range(len(str_2)):
        result.append(str(lst_1[i]))
        result.append(str_2[i])
    result.append(str(lst_1[-1]))
    return ''.join(result)
​
​
​
​
def countdown(operands, target):
    lst_operands = permutation_operands([], list(operands), [], [])
    lst_operators = permutation_operators_backtracking([], ["+", "-", "*", "//"], [], len(operands) - 1)
    for item in lst_operands:
        for combo in lst_operators:
            result = string_join(item, combo)
            if eval(result) == target:
                return result
    return None

