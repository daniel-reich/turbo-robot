"""


A frog wants to cross a river. Unfortunately, he can't jump across in a single
leap. Luckily, there are `n` stones in the river.

The frog can jump from the near bank to stone `1` and from stone `n` to the
far bank. He can also jump from stone to stone, forward and backward. However,
on each stone, a number `j` is written and he must only jump exactly `j`
stones backward or forward.

Return the minimum number of jumps to cross the river (including jumps to the
first stone and from the last stone (or any other stone, if possible) to the
far bank) or `no chance :-(` if it's not possible to cross the river.

### Examples

    jumping_frog(5, [1, 1, 1, 1, 1]) ➞ 6
    
    jumping_frog(5, [1, 3, 1, 1, 1]) ➞ 4
    
    jumping_frog(5, [1, 1, 0, 1, 1]) ➞ "no chance :-("

### Notes

  * The frog may also reach the far bank from another stone than `n` if a large enough number is written on it.
  * `n` is at least 2.

"""

def jumping_frog(n, stones):
    if n < 2:
        return None
    jmpCount = 1 # one jump from the left bank to 1st element
    i = 0
    while i < (n - 1): # visit each stone except the last, (n-1) is the last stone
        distanceToEnd = (n - 1) - i
        jmpValue = stones[i]
        #can we jump ahead? i.e (is there a distance to last stone)
        if 0 < jmpValue <= distanceToEnd:
            # check if we can jump backward ("we did'n reach left bank")
            if (i - jmpValue) >= 0 and stones[i - jmpValue] - 2 * jmpValue > stones[i + jmpValue]:
                i -= jmpValue
            else:
                i += jmpValue
            # increase jump counter
            jmpCount += 1
            # if distance == 0, we reached the end
            if (n - 1) - i == 0:
                return jmpCount + 1
        elif 0 < jmpValue > distanceToEnd: #if stone has abig num to cross the right bank
            return jmpCount + 1
        elif jmpValue == 0 and distanceToEnd > 0: #if we got stuck on a zero num before the end 
            return "no chance :-("

