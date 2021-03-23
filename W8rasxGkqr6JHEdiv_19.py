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

def countdown(operands, target):   
    sign = ["+", "-", "*", "//"]
    for i in range(4):
        for o1 in range(len(operands)):
            for o2 in range(len(operands)):     
                if len(operands) > 2:
                    for o3 in range(len(operands)):
                        for j in range(4):
                            if len(operands) > 3:
                                for o4 in range(len(operands)):    
                                    for k in range(4):
                                        if len(operands) > 4:
                                            for o5 in range(len(operands)):
                                                for l in range(4):
                                                    if o1 != o2 != o3 != o4 != o5 and o3 != o1 != o4 and o4 != o2 != o5 and o1 != o5 != o3:
                                                        result = str(operands[o1])+sign[i]+str(operands[o2])+sign[j]+str(operands[o3])+sign[k]+str(operands[o4])+sign[l]+str(operands[o5])
                                                        if eval(result) == target:
                                                            return result
                                        else:
                                            if o1 != o2 != o3 != o4 and o3 != o1 != o4 and o2 != o4:
                                                result = str(operands[o1])+sign[i]+str(operands[o2])+sign[j]+str(operands[o3])+sign[k]+str(operands[o4])
                                                if eval(result) == target:
                                                    return result
                            else:
                                if o1 != o2 != o3 and o3 != o1:
                                    result = str(operands[o1])+sign[i]+str(operands[o2])+sign[j]+str(operands[o3])
                                    if eval(result) == target:
                                        return result
                else:
                    if o1 != o2:
                        result = str(operands[o1])+sign[i]+str(operands[o2])
                        if eval(result) == target:
                            return result

