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

from collections import deque, defaultdict
def jumping_frog(n, stones):
    voisins = dict()
    for i,jump in enumerate(stones):
        v = []
        if i-jump >= 0:
            v.append(i-jump)
        v.append(min(n,i+jump))
        voisins[i] = v
    unvisited = defaultdict(lambda : True)
    queue = deque()
    distance = defaultdict(int)
    distance[0] = 1
    queue.appendleft(0)
    unvisited[0] = False
    while len(queue) > 0:
        newstone = queue.pop()
        if newstone == n:
            return distance[newstone]
        for voisin in voisins[newstone]:
            if unvisited[voisin]:
                distance[voisin] = distance[newstone] + 1
                unvisited[voisin] = False
                queue.appendleft(voisin)
    return "no chance :-("

