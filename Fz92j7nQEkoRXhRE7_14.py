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

def jumping_frog(stones,lst):
    i,jumps=0,[]
    while i<(stones):
        if i == stones:break
        elif lst[i]==0:return ("no chance :-(")
        if i not in jumps:jumps.append(i)
        if (i<stones-2):
         if lst[i-1]>lst[i] and lst[i-1]>lst[i+1]:
            jumps.append(i - 1)
            i=i-1
            continue
         if i>=stones:
                jumps.append(i)
                break
        i = i + lst[i]
    return len(jumps)+1

