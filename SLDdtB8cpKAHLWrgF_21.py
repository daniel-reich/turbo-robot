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

def permutation(cur, list_to_permutation, used_indexes, result_of_permutation):
    if len(cur) == len(list_to_permutation):
        result_of_permutation.append(cur[:])
    for i in range(len(list_to_permutation)):
        if i in used_indexes:
            continue
        cur.append(list_to_permutation[i])
        used_indexes.append(i)
        permutation(cur, list_to_permutation, used_indexes, result_of_permutation)
        cur.pop()
        used_indexes.pop()
    return result_of_permutation
    
def greater_permutation(expr, nums):
    result_of_permutation_of_nums = permutation([], nums, [], [])
    max_value = eval(((expr.replace("a", str(result_of_permutation_of_nums[0][0]))).replace("b", str(result_of_permutation_of_nums[0][1]))).replace("c", \
                                    str(result_of_permutation_of_nums[0][2])))
    if int(eval(((expr.replace("a", str(result_of_permutation_of_nums[0][0]))).replace("b", str(
            result_of_permutation_of_nums[0][1]))). \
                        replace("c", str(result_of_permutation_of_nums[0][2])))) == eval(((
                        expr.replace("a", str(result_of_permutation_of_nums[0][0]))).replace("b",
                                                                         str(result_of_permutation_of_nums[0][1]))). \
                                                                                                 replace("c", str(result_of_permutation_of_nums[0][2]))):
            final_result = ((expr.replace("a", str(result_of_permutation_of_nums[0][0]))) \
                        .replace("b", str(result_of_permutation_of_nums[0][1]))).replace("c", str(
                        result_of_permutation_of_nums[0][2])) \
                       + " = " + str(int(eval(((expr.replace("a", str(result_of_permutation_of_nums[0][0]))).replace(
                       "b", str(result_of_permutation_of_nums[0][1]))).replace("c", \
                                                                    str(result_of_permutation_of_nums[0][2])))))
​
​
    else:
        final_result = ((expr.replace("a", str(result_of_permutation_of_nums[0][0]))) \
                        .replace("b", str(result_of_permutation_of_nums[0][1]))).replace("c", str(
            result_of_permutation_of_nums[0][2])) \
                       + " = " + str(
            round(float(eval(((expr.replace("a", str(result_of_permutation_of_nums[0][0]))).replace(
                "b", str(result_of_permutation_of_nums[0][1]))).replace("c", \
                                                                        str(result_of_permutation_of_nums[0][2])))), 2))
​
    for i in range(1, len(result_of_permutation_of_nums)):
        if max_value < eval(((expr.replace("a", str(result_of_permutation_of_nums[i][0])))\
                                         .replace("b", str(result_of_permutation_of_nums[i][1]))).replace("c", str(result_of_permutation_of_nums[i][2]))):
            max_value = eval(((expr.replace("a", str(result_of_permutation_of_nums[i][0])))\
                                         .replace("b", str(result_of_permutation_of_nums[i][1]))).replace("c", str(result_of_permutation_of_nums[i][2])))
            if int(eval(((expr.replace("a", str(result_of_permutation_of_nums[i][0]))).replace("b", str(result_of_permutation_of_nums[i][1]))).\
                                replace("c", str(result_of_permutation_of_nums[i][2])))) == eval(((expr.replace("a", str(result_of_permutation_of_nums[i][0]))).replace("b", str(result_of_permutation_of_nums[i][1]))).\
                                replace("c", str(result_of_permutation_of_nums[i][2]))):
                      final_result = ((expr.replace("a", str(result_of_permutation_of_nums[i][0])))\
                                         .replace("b", str(result_of_permutation_of_nums[i][1]))).replace("c", str(result_of_permutation_of_nums[i][2])) \
                           + " = " + str(int(eval(((expr.replace("a", str(result_of_permutation_of_nums[i][0]))).replace(
                                        "b", str(result_of_permutation_of_nums[i][1]))).replace("c", \
                                                                        str(result_of_permutation_of_nums[i][2])))))
​
​
            else:
                final_result = ((expr.replace("a", str(result_of_permutation_of_nums[i][0]))) \
                                .replace("b", str(result_of_permutation_of_nums[i][1]))).replace("c", str(
                    result_of_permutation_of_nums[i][2])) \
                               + " = " + str(round(float(eval(((expr.replace("a", str(result_of_permutation_of_nums[i][0]))).replace(
                    "b", str(result_of_permutation_of_nums[i][1]))).replace("c", \
                                                                            str(result_of_permutation_of_nums[i][2])))), 2))
​
    return final_result

