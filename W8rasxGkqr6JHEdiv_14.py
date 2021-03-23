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

from itertools import combinations_with_replacement, permutations
def countdown(operands, target):
    ops = ['+', '-', '*', '//']
    n_ops = len(operands) - 1
    for p_oper in permutations(operands):
        for comb in combinations_with_replacement(ops, n_ops):
            for p_ops in permutations(comb):
                res = ''
                for i in range(n_ops):
                    res += str(p_oper[i]) + p_ops[i]
                res += str(p_oper[-1])
                if eval(res) == target:
                    return res
    return ''

