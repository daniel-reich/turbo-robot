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
    v = [0]
    loc = 0
    ctr = 1
​
    while loc < n:
        if stones[loc] == 0:
            ctr = 999
            break
        elif loc + stones[loc] not in v:
            loc += stones[loc]
            v.append(loc)
            ctr += 1
        elif v.count(loc + stones[loc]) < 2:
            loc += stones[loc]
            v.append(loc)
            ctr += 1
        elif loc - stones[loc] >= 0:
            if loc - stones[loc] not in v:
                loc -= stones[loc]
                v.append(loc)
                ctr += 1
            elif v.count(loc - stones[loc]) < 2:
                loc -= stones[loc]
                v.append(loc)
                ctr += 1
        else:
            ctr = 999
            break
​
    v = [0]
    loc = 0
    ctr2 = 1
​
    while loc < n:
        if stones[loc] == 0:
            ctr2 = 999
            break
        elif loc - stones[loc] >= 0:
            if loc - stones[loc] not in v:
                loc -= stones[loc]
                v.append(loc)
                ctr2 += 1
            elif v.count(loc - stones[loc]) < 2:
                loc -= stones[loc]
                v.append(loc)
                ctr2 += 1
        if loc + stones[loc] not in v:
            loc += stones[loc]
            v.append(loc)
            ctr2 += 1
        elif v.count(loc + stones[loc]) < 2:
            loc += stones[loc]
            v.append(loc)
            ctr2 += 1
        else:
            ctr2 = 999
            break
​
    if ctr < ctr2:
        return ctr
    elif ctr2 < ctr:
        return ctr2
    elif ctr == 999:
        return 'no chance :-('
    else:
        return ctr

