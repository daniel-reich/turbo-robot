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

def jumping_frog(n, s):
    p = s[0]; c = 2
    while p <= n-1:
        if s[p] == 0:
            return 'no chance :-('
        else:
            if p + s[p] == n-1:
                return c + 2
            elif p + s[p] > n-1:
                return c + 1
            else:
                if p + s[p] + s[p+s[p]] >= p - s[p] + s[p-s[p]]:
                    c += 2
                    p += s[p] + s[p+s[p]]
                else:
                    c += 2
                    p += (-s[p] + s[p-s[p]])
    else: 
        return c

