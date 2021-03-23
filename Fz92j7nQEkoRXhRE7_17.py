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

def jumping_frog(n, stns):
  def update(d,stlst):
    sortlst = sorted(stlst, key = lambda x: d[x])
    j = sortlst[0]
    if d[j] > n:
      return "no chance :-("
    if stns[j]+j >= n:
      return d[j]+1
    d[stns[j]+j] = min(d[stns[j]+j],d[j]+1)
    if j-stns[j] >=0:
      d[j-stns[j]] = min(d[j-stns[j]],d[j]+1)
    return update(d,sortlst[1:])
    
  d = {i:(n+1) for i in range(1,n)}
  d[0] = 1
  return update(d,[i for i in range(n)])

