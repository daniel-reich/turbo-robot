"""


This challenge is based on the classic videogame "Snake".

Assume the game screen is an `n * n` square, and the snake starts the game
with length `1` (i.e. just the head) positioned on the top left corner.

For example, if `n = 7` the game looks something like this:

![](https://edabit-challenges.s3.amazonaws.com/glbiwtu.png)

In this version of the game, the length of the snake doubles each time it eats
food (e.g. if the length is 4, after eating it becomes 8).

Create a function that takes the side `n` of the game screen and returns
_**the number of times the snake can eat before it runs out of space**_ in the
game screen.

### Examples

    snakefill(3) ➞ 3
    
    snakefill(6) ➞ 5
    
    snakefill(24) ➞ 9

### Notes

The given number will always be a positive integer (there are no exceptions to
handle).

"""

def snakefill(n):
    if n== 2:
        return 2
    cnt = 0
    res = 1
    for x in range(1, n+1):
        res *= 2
        cnt += 1
        if res > n * n:
            return cnt-1

