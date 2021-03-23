"""


In the Recursive Staircase Problem, your task is to find the number of ways of
climbing a staircase of `n` stairs, with a set `s` possible steps. The example
below shows that if `n` was `2` and `s` was `{ 1, 2 }`, the answer would be
`2`:

           _
       _ |2  You could either go from step 0-2 (because the set s contains 2), or
    _ | 1    you could go from 0-1-2 (because the set s contains 1, taking one step at a time).
    0

More examples below.

### Examples

    num_ways(4, { 1, 2 }) ➞ 5
    
    num_ways(3, { 1, 2, 3 }) ➞ 4
    
    num_ways(10, { 1, 2, 3, 4 }) ➞ 401

### Notes

The more efficient your solution the better. Do not use unecessary recursion
as this will mean the program needs far longer to complete the tests.

"""

def backtracking_stairs(cur, list_to_permutation, result_of_stairs, target):
    if sum(cur) == target:
        result_of_stairs.append(list(cur[:]))
    if sum(cur) > target:
        return
    for i in range(0, len(list_to_permutation)):
        cur.append(list_to_permutation[i])
        backtracking_stairs(cur, list_to_permutation, result_of_stairs, target)
        cur.pop()
    return result_of_stairs
​
def ways_to_climb(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a+b
    return a
​
def num_ways(n, s):
    if s == {1, 2}:
        return ways_to_climb(n)
    return len(backtracking_stairs([], list(s), [], n))

