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

def jumping_frog_recursive(
        stones,
        frog_position,
        previous_positions):
​
    def get_new_position_options(stones, frog_position):
        if frog_position < 0:
            return[0]
        else:
            j = stones[frog_position]
            if j == 0:
                return []
            new_position_options = []
            if j <= frog_position:
                new_position_options.append(frog_position - j)
            new_position_options.append(frog_position + j)
            return new_position_options
    
    if frog_position >= len(stones):
        return len(previous_positions)
    elif frog_position in previous_positions:
        return None
    else:
        new_position_options = get_new_position_options(stones, frog_position)
        shortest_path = None
        for new_frog_position in new_position_options:
            path = jumping_frog_recursive(
                stones,
                new_frog_position,
                previous_positions + [frog_position])
            if shortest_path is None or (path is not None and path < shortest_path):
                shortest_path = path
        return shortest_path
​
def jumping_frog(n, stones):
    return jumping_frog_recursive(stones, -1, []) or "no chance :-("

