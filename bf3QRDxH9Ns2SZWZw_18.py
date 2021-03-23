"""


In this challenge you will be given a rectangular list representing a "map"
with three types of spaces:

  *  **"+" bombs:** When activated, their explosion activates any bombs directly above, below, left, or right of the "+" bomb.
  *  **"x" bombs:** When activated, their explosion activates any bombs placed in any of the four diagonal directions next to the "x" bomb.
  * Empty spaces "0".

Consider the grid:

    [
      ["+", "+", "0", "x", "x", "+", "0"],
      ["0", "+", "+", "x", "0", "+", "x"]
    ]

If the top left "+" bomb explodes, the resulting chain reaction will blow up
bombs in the order given by the numbers below:

    [
      ["1", "2", "0", "x", "6", "8", "0"],
      ["0", "3", "4", "5", "0", "7", "8"]
    ]

Note that there are two 8's since two of the bombs explode at the same time.
Also, note that one of the "x" bombs in the top row does not explode.

Write a function that determines if the chain reaction started when the _top
left bomb_ explodes destroys all bombs or not.

### Examples

    all_explode([
      ["+", "+", "+", "+", "+", "+", "x"]
    ]) ➞ True
    
    all_explode([
      ["+", "+", "+", "+", "+", "0", "x"]
    ]) ➞ False
    
    all_explode([
      ["+", "+", "0", "x", "x", "+", "0"],
      ["0", "+", "+", "x", "0", "+", "x"]
    ]) ➞ False
    
    all_explode([
      ["x", "0", "0"],
      ["0", "0", "0"],
      ["0", "0", "x"]
    ]) ➞ False
    
    all_explode([
      ["x", "0", "x"],
      ["0", "x", "0"],
      ["x", "0", "x"]
    ]) ➞ True

### Notes

  * Both "+" and "x" bombs have an "explosion range" of 1.
  * Part #2 can be [found here](https://edabit.com/challenge/8tDW5gt4SAX2LKALJ).

"""

def all_explode_prep(grid):
    result = []
    for _ in range(len(grid)):
        result.append([" " for _ in range(len(grid[0]))])
    if grid[0][0] == "+":
        result[0][0] = "boom+"
        grid[0][0] = 'boom+'
    elif grid[0][0] == "x":
        result[0][0] = "boomx"
        grid[0][0] = "boomx"
    else:
        result[0][0] = grid[0][0]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "boom+":
                result[i][j] = "boom+"
            elif grid[i][j] == "boomx":
                result[i][j] = "boomx"
​
    for i in range(len(result)):
        for j in range(len(result[0])):
            if grid[i][j] == "+":
                if j - 1 >= 0 and result[i][j-1] == "boom+":
                    result[i][j] = "boom+"
                elif j + 1 < len(grid[0]) and result[i][j+1] == "boom+":
                    result[i][j] = "boom+"
                elif i - 1 >= 0 and result[i-1][j] == "boom+":
                    result[i][j] = "boom+"
                elif i + 1 < len(grid) and result[i+1][j] == "boom+":
                    result[i][j] = "boom+"
                elif i - 1 >= 0 and j - 1 >= 0 and result[i-1][j-1] == "boomx":
                    result[i][j] = "boom+"
                elif i + 1 < len(grid) and j + 1 < len(grid[0]) and result[i+1][j+1] == "boomx":
                    result[i][j] = "boom+"
                elif i-1>=0 and j + 1 < len(grid[0]) and result[i-1][j+1] == "boomx":
                    result[i][j] = "boom+"
                elif i+1 < len(grid) and j - 1 >= 0 and result[i+1][j-1] == "boomx":
                    result[i][j] = "boom+"
                else:
                    result[i][j] = grid[i][j]
​
            elif grid[i][j] == "x":
                if j - 1 >= 0 and result[i][j-1] == "boom+":
                    result[i][j] = "boomx"
                elif j + 1 < len(grid[0]) and result[i][j+1] == "boom+":
                    result[i][j] = "boomx"
                elif i - 1 >= 0 and result[i-1][j] == "boom+":
                    result[i][j] = "boomx"
                elif i + 1 < len(grid) and result[i+1][j] == "boom+":
                    result[i][j] = "boomx"
                elif i - 1 >= 0 and j - 1 >= 0 and result[i-1][j-1] == "boomx":
                    result[i][j] = "boomx"
                elif i + 1 < len(grid) and j + 1 < len(grid[0]) and result[i+1][j+1] == "boomx":
                    result[i][j] = "boomx"
                elif i-1>=0 and j + 1 < len(grid[0]) and result[i-1][j+1] == "boomx":
                    result[i][j] = "boomx"
                elif i+1 < len(grid) and j - 1>= 0 and result[i+1][j-1] == "boomx":
                    result[i][j] = "boomx"
                else:
                    result[i][j] = grid[i][j]
            else:
                result[i][j] = grid[i][j]
    if result == grid:
        return result
    return all_explode_prep(result)
​
def all_explode(grid):
    return True if all(all_explode_prep(grid)[i][j] != "x" and all_explode_prep(grid)[i][j] != "+" for i in range(len(grid)) for j in range(len(grid[0]))) else False

