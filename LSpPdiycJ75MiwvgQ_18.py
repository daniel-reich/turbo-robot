"""


How many ways are there to navigate through a grid `(w * h)`?

![Grid](https://edabit-challenges.s3.amazonaws.com/grid_paths.png)

Suppose you're on a 4 × 6 grid, and want to go from the bottom left to the top
right. How many different paths can you take? Avoid backtracking, you can only
move right or up.

Create a function that takes `w`idth and `h`eight and returns the amount of
possibilities.

### Examples

    grid_pos([1, 1]) ➞ 2
    
    grid_pos([6, 4]) ➞ 210
    
    grid_pos([5, 5]) ➞ 252

### Notes

Check the **Resources** tab for a detailed explanation.

"""

def grid_pos(lst):
    def factorial(x):
        if x<=1:
            return 1
        return x*factorial(x-1)
    return factorial(sum(lst))/factorial(lst[0])/factorial(lst[1])

