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

from collections import deque
def jumping_frog(n, stones):
  exits = [i for i in range(n) if i + stones[i] >= n]
  distances = {i : 1 for i in exits}
  q =  deque(exits)
  while q and 0 not in distances:
    cur = q.popleft()
    neighbors = [i for i in range(n) if i not in distances and(
                                      i + stones[i] == cur or 
                                       i - stones[i] == cur)]
    for nbr in neighbors:
      distances[nbr] = distances[cur] + 1
      q.append(nbr)
  return distances[0] + 1 if 0 in distances else 'no chance :-('

