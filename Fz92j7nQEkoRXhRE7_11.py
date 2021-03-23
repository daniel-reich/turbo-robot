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
  i,jumps, unresolvable_spot, bad_spaces, hyper_jump=0,1,[],[],[]
  for j in range(len(stones)):
    if(j+stones[j]<len(stones)):
      if (stones[i]==0 or stones[j+stones[j]]==0):
        bad_spaces.append(j)
    if (j+stones[j]>=len(stones) and j< len(stones)-1):
      hyper_jump.append(j)
  while i<len(stones):
    if (i+stones[i] not in bad_spaces):
      i+=stones[i]
      jumps+=1
      if (i<len(stones)-1):
        if(i-stones[i]>=0):
          if (i-stones[i] in hyper_jump):
            i-=stones[i]
            jumps+=1
            i+=stones[i]
            jumps+=1
    else:
      unresolvable_spot.append(i)
      i-=stones[i]
      jumps+=1
      if(i<0):
        return ("no chance :-(")
    if (i in unresolvable_spot):
      return ("no chance :-(")
  return jumps

